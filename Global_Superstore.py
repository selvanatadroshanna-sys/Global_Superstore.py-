
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(page_title='Global_Superstore',layout='wide')
@st.cache_data
def load_data():
    df = pd.read_csv('df_clean.csv')
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])
    return df

df = load_data()

Categorical=['ship_mode','customer_name','segment','country','city','state','region','category','sub-category','product_name','market','order_priority']
Numerical=['sales','quantity','discount','profit','shipping_cost']

# Sidebar Navigation
page = st.sidebar.radio(
    "Navigation",
    [   "Home",
        "Summary Dashboard",
        "Detailed Analysis",
        "Insights & Recommendations"
    ]
)

if page == "Home":
    st.markdown(
        f"""
        <style>
        .hero {{
            position: relative;
            height: 80vh;
            background-image: url("https://img.freepik.com/premium-photo/store-with-lot-cans-beer-shelf_939033-80225.jpg?semt=ais_hybrid&w=740&q=80");
            background-size: cover;
            background-position: center;
        }}

        .hero::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            backdrop-filter: blur(3px);
            background: rgba(0,0,0,0.4);
        }}

        .hero-content {{
            position: relative;
            z-index: 1;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
        }}

        .hero h1 {{
            font-size: 50px;
            margin-bottom: 10px;
        }}

        .hero p {{
            font-size: 20px;
            color: #ddd;
        }}
        </style>

        <div class="hero">
            <div class="hero-content">
                <h1>Global Superstore Dashboard</h1>
                <p>Analyze sales, profit, customers, and performance across regions and years.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

region_filter=st.sidebar.multiselect('Region',options=df['region'].unique(),default=df['region'].unique())
df['year']=df['order_date'].dt.year
minyear,maxyear=st.sidebar.slider('Years',int(df['year'].min()),int(df['year'].max()),(int(df['year'].min()),int(df['year'].max())))
filtered_df = df[df['region'].isin(region_filter)&(df['year'].between(minyear,maxyear))]


# 1. Summary Dashboard for Top Management

if page == "Summary Dashboard":
    st.header("Summary Dashboard")

    # KPIs
    # Total Sales, Profit, Orders, Return Rate
    with st.expander('show data'):
        st.dataframe(filtered_df.head(10))

    col1,col2,col3,col4= st.columns(4)

    total_sales = filtered_df["sales"].sum()
    total_profit = filtered_df["profit"].sum()  
    total_orders = filtered_df["order_id"].nunique()
    return_rate = (filtered_df['returned']=='Yes').mean()

    col1.metric("Total Sales", f"{total_sales:.2f}",)
    col2.metric("Total Profit", f"{total_profit:.2f}")
    col3.metric("Total Orders", f"{total_orders}")
    col4.metric("Return Rate", f"{return_rate*100:.2f}%")

    # High-level charts
    # Sales over time
    filtered_df['month'] = filtered_df['order_date'].dt.to_period('M').astype(str)
    sales_by_month = filtered_df.groupby('month')['sales'].sum().reset_index(name='sales')
    sales_by_month.columns = ['month', 'sales']
    fig=px.line(sales_by_month, x='month', y='sales',title='Total Sales by Month',color_discrete_sequence=["#2E8B57"])
    st.plotly_chart(fig,use_container_width=True)
    # Sales by Market
    sales_by_market=filtered_df.groupby('market')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
    fig2=px.bar(sales_by_market, x='market', y='sales', title='Top 10 Markets by Revenue',color_discrete_sequence=["#1F77B4"])
    st.plotly_chart(fig2,use_container_width=True)
# =========================
# 2. Detailed Analysis
# =========================
elif page == "Detailed Analysis":
    st.header("Detailed Analysis")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Sales",
        "Profit & Discount",
        "Returns",
        "Customers",
        "Managers",
        "Shipping"
    ])

    with tab1:
        st.subheader("Sales Analysis")
        # Sales by year
        sales_by_year = filtered_df.groupby(filtered_df['order_date'].dt.year)['sales'].sum().reset_index(name='sales')
        sales_by_year.columns = ['year', 'sales']
        fig=px.line(sales_by_year, x='year', y='sales',title='Total Sales by Year',color_discrete_sequence=["#2E8B57"])
        fig.update_xaxes(tickmode='linear', dtick=1)
        st.plotly_chart(fig,use_container_width=True)
        # Sales by category
        sales_by_category=filtered_df.groupby('category')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
        fig8=px.bar(sales_by_category, x='category', y='sales', title='Sales by Category',color_discrete_sequence=["#2A9D8F"])
        st.plotly_chart(fig8,use_container_width=True)
        # Top products
        top_products=filtered_df.groupby('product_name')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
        fig9=px.bar(top_products, x='product_name', y='sales', title='Top 10 Products by Revenue',color_discrete_sequence=["#4C78A8"])
        st.plotly_chart(fig9,use_container_width=True)

    with tab2:
        st.subheader("Profit & Discount Analysis")
        col1,col2= st.columns(2)
        # Category by Profit
        with col1:
            cat_profit=filtered_df.groupby('category')['profit'].sum().reset_index().sort_values(by='profit',ascending=False)
            fig17=px.bar(cat_profit,x='category',y='profit',title='category by profit',color_discrete_sequence=["#1F77B4"])
            st.plotly_chart(fig17,use_container_width=True)  
        # Discount analysis
        with col2:
            cat_discount=filtered_df.groupby('category')['discount'].mean().reset_index().sort_values(by='discount',ascending=False)
            fig5=px.bar(cat_discount,x='category',y='discount',title='category by average discount',color_discrete_sequence=["#F4A261"])
            st.plotly_chart(fig5,use_container_width=True)
        # Loss sub-categories
        loss_bysubcat=filtered_df[filtered_df['profit'] < 0].groupby('sub-category')['profit'].sum().reset_index().sort_values(by='profit')
        fig6=px.bar(loss_bysubcat,x='sub-category',y='profit',title='loss_bysubcat' )
        st.plotly_chart(fig6,use_container_width=True)
    with tab3:

        st.subheader("Returns Analysis")
        col1,col2= st.columns(2)
        # Return rate by region
        with col1:
            return_rate_by_region = filtered_df.groupby('region')['returned'].apply(lambda x: (x == 'Yes').mean()).reset_index().sort_values(by='returned', ascending=False).head(10)
            fig11=px.bar(return_rate_by_region,x='region',y='returned',title='Top 10 Regions by Return Rate',color_discrete_sequence=["#D62728"])
            st.plotly_chart(fig11,use_container_width=True)
        # Returns by category
        with col2:
            return_rate_by_categ = filtered_df.groupby('category')['returned'].apply(lambda x: (x == 'Yes').mean()).reset_index().sort_values(by='returned', ascending=False).head(10)
            fig12=px.bar(return_rate_by_categ,x='category',y='returned',title='Top 10 categories by Return Rate',color_discrete_sequence=["#E76F51"])
            st.plotly_chart(fig12,use_container_width=True)

    with tab4:
        st.subheader("Customer & Segment Analysis")
        # Sales by segment
        segment_sales=filtered_df.groupby('segment')['sales'].sum().reset_index().sort_values(by='sales',ascending=False)
        fig10=px.bar(segment_sales,x='segment',y='sales',title='Sales by Customer Segment')
        st.plotly_chart(fig10,use_container_width=True)
        #most_active_person
        filtered_df['month'] = filtered_df['order_date'].dt.to_period('M').astype(str)
        most_active_person=filtered_df.groupby([filtered_df['region'], filtered_df['month'] , filtered_df['person']])['order_id'].count().reset_index(name='order_count').sort_values(by=['region', 'order_count'], ascending=[True, False])
        most_active_person=most_active_person.groupby('region').head(1)
        fig13=px.bar(most_active_person,x='person',y='order_count',title='Most Active Person by Region',color_discrete_sequence=["#6F42C1"])
        st.plotly_chart(fig13,use_container_width=True)
        # Avg order value
        avg_order_value = filtered_df.groupby('order_id')['sales'].sum().mean()
        st.metric("Avg Order Value", f"{avg_order_value:.2f}")
    with tab5:
        st.subheader("Regional Manager Performance")
        # Sales by person
        sales_by_person=filtered_df.groupby('person')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
        fig14=px.bar(sales_by_person, x='person', y='sales', title='Sales by Person')
        st.plotly_chart(fig14,use_container_width=True)

        # Profit by person
        profit_by_person=filtered_df.groupby('person')['profit'].sum().reset_index().sort_values(by='profit', ascending=False).head(10)
        fig15=px.bar(profit_by_person, x='person', y='profit', title='Profit by Person')
        st.plotly_chart(fig15,use_container_width=True)
    with tab6:
        st.subheader("Shipping")
        # Ship mode
        fig16=px.histogram(filtered_df,x='ship_mode',title=f'shipping mode')
        st.plotly_chart(fig16,use_container_width=True,color_discrete_sequence=["#6F42C1"])

        # Shipping time
        shipping_by_year = filtered_df.groupby(filtered_df['ship_date'].dt.year)['shipping_cost'].sum().reset_index()
        shipping_by_year.columns = ['year', 'shipping_cost']
        fig18=px.line(shipping_by_year, x='year', y='shipping_cost',title='Total shipping by Year',color_discrete_sequence=["#8A63D2"])
        fig18.update_xaxes(tickmode='linear', dtick=1)
        st.plotly_chart(fig18,use_container_width=True)
        # Shipping cost
        Total_shipping_cost = filtered_df['shipping_cost'].sum()
        st.metric("Total Shipping Cost", f"{Total_shipping_cost:.2f}")


# =========================
# 3. Insights & Recommendations
# =========================
elif page == "Insights & Recommendations":
    st.header("Insights & Recommendations")

    # Key Insights
    # Business Problems
    # Recommendations

