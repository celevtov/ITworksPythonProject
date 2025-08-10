#import project files
import helper
 
#import third-party libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def getMonthDates(whole_month=1, onlystart=0, date_name='start date'):
    start_dt = end_dt = pd.NaT
    while pd.isna(start_dt):
        print(f'Enter the {date_name} in DD-MM-YYYY format:')
        str_start_dt=input('>>')
        try:
            start_dt=pd.to_datetime(str_start_dt, format="%d-%m-%Y")
            #shift to the 1st day of month if needed
            if whole_month==1:
                start_dt_m=start_dt.to_period('M').start_time
                if start_dt_m.date() != start_dt.date():
                    print(f'We will use {start_dt_m.strftime("%d-%m-%Y")} as the start month date to get full month')
                    start_dt=start_dt_m
        except ValueError as Ex:
            print(f'Error {type(Ex)} {Ex}')
        except Exception as Ex: raise Ex
    if onlystart==1:
        end_dt=start_dt.to_period('M').end_time
    else:
        while pd.isna(end_dt):
            print('Enter the end date in DD-MM-YYYY format:')
            str_end_dt=input('>>')
            try:
                end_dt=pd.to_datetime(str_end_dt, format="%d-%m-%Y")
                #check if end date > start date
                if end_dt < start_dt:
                    print('End date should be bigger than start date. Try again')
                    end_dt = pd.NaT
                #shift to the 1st day of month if needed
                if whole_month==1:
                    end_dt_m=end_dt.to_period('M').end_time
                    if end_dt_m.date() != end_dt.date():
                        print(f'We will use {end_dt_m.strftime("%d-%m-%Y")} as the end date to get full month')
                        end_dt=end_dt_m
            except ValueError as Ex:
                print(f'Error {type(Ex)} {Ex}')
            except Exception as Ex: raise Ex
    
    return start_dt, end_dt

def salesmarginprc(sales_df_proc):
    start_date, end_date = getMonthDates()
    sales_dt_filtered=sales_df_proc.loc[(sales_df_proc['Order_Month']>=start_date)&(sales_df_proc['Order_Month']<=end_date)]
    #sales_dt_filtered['Margin_Prc1']=sales_dt_filtered['Profit']/sales_dt_filtered['Sales']*100
    #print(sales_dt_filtered.head())
    sales_margin_grouped=pd.DataFrame(sales_dt_filtered.groupby('Order_Month').aggregate({'Sales':'sum', 'Profit':'sum'}).round(2).reset_index()) #, 'Margin_Prc':sum}))
    #print(sales_margin_grouped.info())
    sales_margin_grouped['Margin_Prc']=(sales_margin_grouped['Profit']/sales_margin_grouped['Sales']*100).round(2)
    #print(sales_margin_grouped)

# ADD ??? bottom 10 margin% days in period
    plt.plot(sales_margin_grouped['Order_Month'], sales_margin_grouped['Sales'], label='Sales', color='tab:blue')
    plt.plot(sales_margin_grouped['Order_Month'], sales_margin_grouped['Profit'], label='Profit', color='tab:orange')
    #plt.plot(sales_margin_grouped['Order_Date'], sales_margin_grouped['Margin_Prc'], label='Margin %', color='tab:orange')
    plt.xticks(rotation='vertical')
    plt.xlabel("Month")
    plt.ylabel("Sales/Profit, $")
# ADD legenda
    plt.title(f'Monthly Sales and Profit for {start_date.strftime("%d-%m-%Y")} - {end_date.strftime("%d-%m-%Y")}')
    plt.legend()
    plt.show()


def topbottomproducts(sales_df_proc):
    start_date, end_date = getMonthDates(whole_month=0)
    sales_dt_filtered=sales_df_proc.loc[(sales_df_proc['Order_Date']>=start_date)&(sales_df_proc['Order_Date']<=end_date)]
    subcat_grouped_top5=pd.DataFrame(sales_dt_filtered.groupby('Sub-Category', observed=True)['Sales'].sum().sort_values(ascending=False).head(5).reset_index())
    subcat_grouped_bottom5=pd.DataFrame(sales_dt_filtered.groupby('Sub-Category', observed=True)['Sales'].sum().sort_values(ascending=False).tail(5).reset_index())
    #print(subcat_grouped_top5)
    #print(subcat_grouped_bottom5)
    
    fig, axs = plt.subplots(2)

# ADD sales values on the bars    
    bar1=axs[0].bar(subcat_grouped_top5['Sub-Category'], subcat_grouped_top5['Sales'], color='tab:blue')
    axs[0].set_title(f'TOP-5 Product Sub-categories for {start_date.strftime("%d-%m-%Y")} - {end_date.strftime("%d-%m-%Y")}')
    axs[0].set_xlabel('days')
    axs[0].set_ylabel('Sales')
    axs[0].bar_label(bar1, label_type='center', fmt='%.2f', fontsize=10, color='black')

    bar2=axs[1].bar(subcat_grouped_bottom5['Sub-Category'], subcat_grouped_bottom5['Sales'], color='tab:orange')
    axs[1].set_title(f'BOTTOM-5 Product Sub-categories for {start_date.strftime("%d-%m-%Y")} - {end_date.strftime("%d-%m-%Y")}')
    axs[1].set_xlabel('days')
    axs[1].set_ylabel('Sales')
    axs[1].bar_label(bar2, label_type='center', fmt='%.2f', fontsize=10, color='black')

    fig.subplots_adjust(hspace=1) #, wspace=2) 
    plt.show()
    
    
def avgmonthlysales(sales_df_proc):
    start_date, end_date = getMonthDates()
    sales_dt_filtered=sales_df_proc.loc[(sales_df_proc['Order_Date']>=start_date)&(sales_df_proc['Order_Date']<=end_date)]
    sales_order_grouped = pd.DataFrame(sales_dt_filtered.groupby(['Segment','Order_Month','Order_ID'], observed=True).aggregate({'Sales': 'sum',
                                 'Product_ID': 'count', 'Quantity': 'sum'}).round(2).reset_index())
# ADD round(2)    
    df_avg_bill=pd.DataFrame(sales_order_grouped.groupby(['Order_Month'])['Sales'].mean().round(2).reset_index())
    bar1=plt.bar(df_avg_bill['Order_Month'], df_avg_bill['Sales'], width=20)
    plt.xticks(rotation='vertical')
    plt.xlabel("Month")
    plt.ylabel("Average Bill")
    plt.title(f'Average monthly Bill for {start_date.strftime("%d-%m-%Y")} - {end_date.strftime("%d-%m-%Y")}')
    plt.bar_label(bar1, label_type='edge', fmt='%.2f', fontsize=10, color='black')
    plt.show()
    #need to delete outliers
    print('''
    
    Average monthly bill by client segments:''')
    print(sales_order_grouped.pivot_table(index='Order_Month', columns='Segment',
                    aggfunc={'Sales':'mean'}, observed=True).round(2))
    #print(sales_order_grouped.groupby(['Segment','Order_Month'])['Sales'].aggregate(['min','mean','max'])) #mean())

def shippingstats(sales_df_proc):
    start_date, end_date = getMonthDates(onlystart=1, date_name='month start date')
    st_index=['First Class', 'Same Day', 'Second Class', 'Standard Class']
    df_ship_times=pd.DataFrame([[1,3],[0,0],[2,4],[4,6]], index=st_index, columns=['min_days','max_days'])
    #print(df_ship_times)
    #print(sales_df_proc.groupby(pd.Grouper(key='dtOrderDate', freq='M')).min())
    sales_dt_filtered=sales_df_proc.loc[(sales_df_proc['Order_Date']>=start_date)&(sales_df_proc['Order_Date']<=end_date)]
    #print(sales_dt_filtered2.head())
    #print(sales_dt_filtered2.info())
    sales_ship_merged=pd.merge(sales_dt_filtered, df_ship_times, how='left', left_on='Ship_Mode', right_index=True)
    sales_ship_merged['Shipping_ontime']=np.where(sales_ship_merged['ShipingSpeed']>sales_ship_merged['max_days'], 0,1)
    ship_delays_grouped=pd.DataFrame(sales_ship_merged.groupby(['State'], observed=True).aggregate({'ShipingSpeed':'count','Shipping_ontime':'sum'}).round(2).reset_index())
    ship_delays_grouped['Shipping_SLA']=(ship_delays_grouped['Shipping_ontime']/ship_delays_grouped['ShipingSpeed']*100).round(2)
    #print(ship_delays_grouped)
    # draw a horisontal bar
    
    ship_SLA = 95
    print(f'Shipping times by shipping mode for {start_date.strftime("%d-%m-%Y")} - {end_date.strftime("%d-%m-%Y")}:'.upper())
    print(sales_ship_merged.groupby(['Ship_Mode','max_days'], observed=True)['ShipingSpeed'].aggregate(['min','mean','max']).round(2))
    print(f'NOTE: current SLA: is {ship_SLA}% of shippings made on time')

    plt.plot(ship_delays_grouped['State'], [ship_SLA for i in range(ship_delays_grouped['State'].size)], label='SLA', color='black', linewidth=3)
    colors = []
    for val in ship_delays_grouped['Shipping_SLA']:
        if val >= ship_SLA:
            colors.append('skyblue')  # Color for values above or equal to threshold
        else:
            colors.append('lightcoral') # Color for values below threshold
    bar1=plt.bar(ship_delays_grouped['State'], ship_delays_grouped['Shipping_SLA'], color=colors)
    xlocs, xlabels = plt.xticks(rotation='vertical')
    for i, xlab in enumerate(xlabels):
        if colors[i]=='skyblue':
            xlab.set_color('black')
        else:
            xlab.set_color(colors[i])
    plt.xlabel("States")
    plt.ylabel("Shipping rate, %")
    plt.title(f'Shipping SLA for {start_date.strftime("%d-%m-%Y")} - {end_date.strftime("%d-%m-%Y")}')
    
    plt.legend()
    plt.show()

    #print(sales_ship_merged.loc[sales_ship_merged['ShipingSpeed']>sales_ship_merged['max_days']].groupby(['Ship_Mode','Order_Month','ShipingSpeed']).aggregate({'ShipingSpeed':'count'}))
    #print('Orders with shipping delays:')
    #print(sales_ship_merged.loc[sales_ship_merged['ShipingSpeed']>sales_ship_merged['max_days']][['Order_ID','Order_Date', 'Ship_Date','State','ShipingSpeed']]) #.groupby([pd.Grouper(key='dtOrderDate', freq='M'),'ShipDays']).aggregate({'ShipDays':'count'}))


def activecustomers(sales_df_proc):
    start_date, end_date = getMonthDates(onlystart=1, date_name='date')
    n_days_sleep=365
    sales_cust_sleep=pd.DataFrame(sales_df_proc.loc[sales_df_proc['Order_Date']<=start_date].groupby(['Customer_ID', 'Customer_Name', 'Segment'], observed=True)['Order_Date'].max().reset_index())
    sales_cust_sleep['no_order_days']=(start_date-sales_cust_sleep['Order_Date']).dt.days
    sales_cust_sleep['is_active']=np.where(sales_cust_sleep['no_order_days']>n_days_sleep, 0, 1)
    #print(sales_cust_sleep.head())
    #print(sales_cust_sleep.info())
    act_cust_grouped=pd.DataFrame(sales_cust_sleep.groupby('Segment', observed=True).aggregate({'is_active':'sum', 'Customer_ID':'count'}).reset_index())
    act_cust_grouped['active_cust_SLA']=(act_cust_grouped['is_active']/act_cust_grouped['Customer_ID']*100).round(2)
#rename column is_active

    activecust_SLA = 85
    print(f'Number of Active customers by segments on {start_date.strftime("%d-%m-%Y")}:'.upper())
    print(act_cust_grouped)
    print(f'NOTE: current SLA is: {activecust_SLA}% of customers are active')
    
    plt.plot(act_cust_grouped['Segment'], [activecust_SLA for i in range(act_cust_grouped['Segment'].size)], label='SLA', color='black', linewidth=3)
    colors = []
    for val in act_cust_grouped['active_cust_SLA']:
        if val >= activecust_SLA:
            colors.append('skyblue')  # Color for values above or equal to threshold
        else:
            colors.append('lightcoral') # Color for values below threshold
    plt.bar(act_cust_grouped['Segment'], act_cust_grouped['active_cust_SLA'], color=colors)
    #plt.xticks(rotation='vertical')
    plt.xlabel("Customer Segments")
    plt.ylabel("Active customers, %")
    plt.title(f'Active customers SLA by segments on {start_date.strftime("%d-%m-%Y")}')

    plt.legend()
    plt.show()

    #sc_segment='Corporate'
    #print(f'List of Sleeping customers for segment {sc_segment}:')
    #print(sales_cust_sleep.loc[(sales_cust_sleep['no_order_days']>n_days_sleep)&(sales_cust_sleep['Segment']==sc_segment)])


def dashboard(sales_df_proc):
    print('Here will be a Big Beautiful Dashboard')


def gencharts(sales_df_proc):
    #print('print data sample')
    #print(sales_df_proc.head())
    while True:
        print('Choose your option:')
        print("""
                    1 - show monthly Sales and Profit/Margin % by period  
                    2 - show Top and Bottom Sales product categories  
                    3 - show Average monthly Bill
                    4 - show Shipping monthly statistics 
                    5 - show Sleeping customers statistics on date
                    Q - return to Main menu  
                  """)
        inp = input('>>')
        if inp =='1':
            salesmarginprc(sales_df_proc)
        elif inp =='2':
            topbottomproducts(sales_df_proc)
        elif inp =='3':
            avgmonthlysales(sales_df_proc)
        elif inp =='4':
            shippingstats(sales_df_proc)
        elif inp =='5':
            activecustomers(sales_df_proc)
        elif inp.upper() =='Q':
            break
        else:
            print(f'No such command: {inp} Try again')
