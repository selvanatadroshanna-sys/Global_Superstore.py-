

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(page_title='Global_Superstore',layout='wide')
st.markdown("""
<style>
/* General App */
.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #eef4ff 100%);
}

/* Main container */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Titles */
h1, h2, h3 {
    color: #0f172a;
    font-weight: 700;
}

/* KPI cards */
.kpi-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border: 1px solid #e2e8f0;
    text-align: center;
}
.kpi-title {
    font-size: 15px;
    color: #64748b;
    margin-bottom: 8px;
}
.kpi-value {
    font-size: 30px;
    font-weight: 700;
    color: #0f172a;
}

/* Section cards */
.custom-card {
    background: rgba(255,255,255,0.92);
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border: 1px solid #e2e8f0;
    margin-bottom: 20px;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}
.stTabs [data-baseweb="tab"] {
    background: #e2e8f0;
    border-radius: 12px;
    padding: 10px 18px;
}
.stTabs [aria-selected="true"] {
    background: #2563eb !important;
    color: white !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1rem;
    font-weight: 600;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #1d4ed8, #1e40af);
    color: white;
}

/* Metric box enhancement */
div[data-testid="metric-container"] {
    background: white;
    border: 1px solid #e2e8f0;
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)
@st.cache_data
def load_data():
    df = pd.read_csv('df_clean.csv')
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])
    return df

df = load_data()
df['month'] = df['order_date'].dt.to_period('M').astype(str)
df['year'] =df['order_date'].dt.year


Categorical=['ship_mode','customer_name','segment','country','city','state','region','category','sub-category','product_name','market','order_priority']
Numerical=['sales','quantity','discount','profit','shipping_cost']
def beautify_fig(fig):
    fig.update_layout(
        template="plotly_white",
        title=dict(font=dict(size=22, color="#0f172a")),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", size=13, color="#334155"),
        margin=dict(l=20, r=20, t=60, b=20),
    )
    fig.update_xaxes(showgrid=False, linecolor="#cbd5e1")
    fig.update_yaxes(showgrid=True, gridcolor="#e2e8f0", linecolor="#cbd5e1")
    return fig

# Sidebar Navigation
page = st.sidebar.radio(
    "Navigation",
    [   "Home",
        "Summary Dashboard",
        "Detailed Analysis",
        "Insights & Recommendations"
    ]
)
st.markdown("""
<div class="custom-card">
    <h1 style="margin-bottom:6px;">Global Superstore Analytics Dashboard</h1>
    <p style="color:#475569; font-size:16px; margin-bottom:0;">
        Interactive business dashboard for analyzing sales, profit, returns, customers, and shipping performance across global markets.
    </p>
</div>
""", unsafe_allow_html=True)
region_filter=st.sidebar.multiselect('Region',options=df['region'].unique(),default=df['region'].unique())
df['year']=df['order_date'].dt.year
minyear,maxyear=st.sidebar.slider('Years',int(df['year'].min()),int(df['year'].max()),(int(df['year'].min()),int(df['year'].max())))
filtered_df = df[df['region'].isin(region_filter)&(df['year'].between(minyear,maxyear))].copy()
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

# 1. Summary Dashboard for Top Management

elif page == "Summary Dashboard":
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

    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Sales</div>
            <div class="kpi-value">${total_sales:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Profit</div>
            <div class="kpi-value">${total_profit:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Orders</div>
            <div class="kpi-value">{total_orders:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Return Rate</div>
            <div class="kpi-value">{return_rate*100:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)


    # Sales over time
    
    sales_by_month = filtered_df.groupby('month')['sales'].sum().reset_index(name='sales')
    sales_by_month.columns = ['month', 'sales']
    fig=px.line(sales_by_month, x='month', y='sales',title='Total Sales by Month')
    fig = beautify_fig(fig)
    st.plotly_chart(fig,use_container_width=True)
    # Sales by Market
    sales_by_market=filtered_df.groupby('market')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
    fig2=px.bar(sales_by_market, x='market', y='sales', title='Top 10 Markets by Revenue')
    fig2 = beautify_fig(fig2)
    st.plotly_chart(fig2,use_container_width=True)


 # 2. Detailed Analysis

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
        sales_by_year = filtered_df.groupby('year')['sales'].sum().reset_index(name='sales')
        sales_by_year.columns = ['year', 'sales']
        fig=px.line(sales_by_year, x='year', y='sales',title='Total Sales by Year')
        fig.update_xaxes(tickmode='linear', dtick=1)
        fig = beautify_fig(fig)
        st.plotly_chart(fig,use_container_width=True)
        # Sales by category
        sales_by_category=filtered_df.groupby('category')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
        fig8=px.bar(sales_by_category, x='category', y='sales', title='Sales by Category')
        fig8 = beautify_fig(fig8)
        st.plotly_chart(fig8,use_container_width=True)
        # Top products
        top_products=filtered_df.groupby('product_name')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
        fig9=px.bar(top_products, x='product_name', y='sales', title='Top 10 Products by Revenue')
        fig9 = beautify_fig(fig9)
        st.plotly_chart(fig9,use_container_width=True)

    with tab2:
        st.subheader("Profit & Discount Analysis")
        col1,col2= st.columns(2)
        # Profit by Category
        with col1:
            cat_profit=filtered_df.groupby('category')['profit'].sum().reset_index().sort_values(by='profit',ascending=False)
            fig17=px.bar(cat_profit,x='category',y='profit',title='Profit by Category')
            fig17 = beautify_fig(fig17)
            st.plotly_chart(fig17,use_container_width=True)  
        # Discount analysis
        with col2:
            cat_discount=filtered_df.groupby('category')['discount'].mean().reset_index().sort_values(by='discount',ascending=False)
            fig5=px.bar(cat_discount,x='category',y='discount',title='category by average discount')
            fig5 = beautify_fig(fig5)
            st.plotly_chart(fig5,use_container_width=True)
        # Loss sub-categories
        loss_bysubcat=filtered_df[filtered_df['profit'] < 0].groupby('sub-category')['profit'].sum().reset_index().sort_values(by='profit')
        fig6=px.bar(loss_bysubcat,x='sub-category',y='profit',title='Loss sub-categories' )
        fig6 = beautify_fig(fig6)
        st.plotly_chart(fig6,use_container_width=True)
    with tab3:
        
        st.subheader("Returns Analysis")
        col1,col2= st.columns(2)
        # Return rate by region
        with col1:
            return_rate_by_region = filtered_df.groupby('region')['returned'].apply(lambda x: (x == 'Yes').mean()).reset_index().sort_values(by='returned', ascending=False).head(10)
            fig11=px.bar(return_rate_by_region,x='region',y='returned',title='Top 10 Regions by Return Rate')
            fig11 = beautify_fig(fig11)
            st.plotly_chart(fig11,use_container_width=True)
        # Returns by category
        with col2:
            return_rate_by_categ = filtered_df.groupby('category')['returned'].apply(lambda x: (x == 'Yes').mean()).reset_index().sort_values(by='returned', ascending=False).head(10)
            fig12=px.bar(return_rate_by_categ,x='category',y='returned',title='Top 10 categories by Return Rate')
            fig12 = beautify_fig(fig12)
            st.plotly_chart(fig12,use_container_width=True)

    with tab4:
        st.subheader("Customer & Segment Analysis")
        # Sales by segment
        segment_sales=filtered_df.groupby('segment')['sales'].sum().reset_index().sort_values(by='sales',ascending=False)
        fig10=px.bar(segment_sales,x='segment',y='sales',title='Sales by Customer Segment')
        fig10 = beautify_fig(fig10)
        st.plotly_chart(fig10,use_container_width=True)
        #most_active_person
        most_active_person=filtered_df.groupby([filtered_df['region'], filtered_df['person']])['order_id'].count().reset_index(name='order_count').sort_values(by=['region', 'order_count'], ascending=[True, False])
        most_active_person=most_active_person.groupby('region').head(1)
        fig13=px.bar(most_active_person,x='person',y='order_count',title='Most Active Person by Region')
        fig13 = beautify_fig(fig13)
        st.plotly_chart(fig13,use_container_width=True)
        # Avg order value
        avg_order_value = filtered_df.groupby('order_id')['sales'].sum().mean()
        st.metric("Avg Order Value", f"{avg_order_value:.2f}")
        
    with tab5:
        st.subheader("Regional Manager Performance")
        # Sales by person
        sales_by_person=filtered_df.groupby('person')['sales'].sum().reset_index().sort_values(by='sales', ascending=False).head(10)
        fig14=px.bar(sales_by_person, x='person', y='sales', title='Sales by Person')
        fig14 = beautify_fig(fig14)
        st.plotly_chart(fig14,use_container_width=True)

        # Profit by person
        profit_by_person=filtered_df.groupby('person')['profit'].sum().reset_index().sort_values(by='profit', ascending=False).head(10)
        fig15=px.bar(profit_by_person, x='person', y='profit', title='Profit by Person')
        fig15 = beautify_fig(fig15)
        st.plotly_chart(fig15,use_container_width=True)
    with tab6:
        st.subheader("Shipping")
        # Ship mode
        fig16=px.histogram(filtered_df,x='ship_mode',title=f'Shipping Mode Distribution')
        fig16 = beautify_fig(fig16)
        st.plotly_chart(fig16,use_container_width=True)

        # Shipping time
        shipping_by_year = filtered_df.groupby(filtered_df['ship_date'].dt.year)['shipping_cost'].sum().reset_index()
        shipping_by_year.columns = ['year', 'shipping_cost']
        fig18=px.line(shipping_by_year, x='year', y='shipping_cost',title='Total shipping by Year')
        fig18.update_xaxes(tickmode='linear', dtick=1)
        fig18 = beautify_fig(fig18)
        st.plotly_chart(fig18,use_container_width=True)
        # Shipping cost
        Total_shipping_cost = filtered_df['shipping_cost'].sum()
        st.metric("Total Shipping Cost", f"{Total_shipping_cost:.2f}")


 # 3. Insights & Recommendations

elif page == "Insights & Recommendations":
    st.header("Insights & Recommendations")

    # Key Insights
    st.subheader("Key Insights")

    st.markdown("""
    -Standard Class is the most commonly used shipping mode, indicating a strong preference for low-cost delivery.
    - The Consumer segment is the dominant and most profitable segment, making it the primary revenue driver.
    - Office Supplies is the most frequent category, showing consistent and recurring demand.
    - Binders is one of the most popular sub-categories in terms of order frequency.
    - The Asia Pacific market shows strong sales presence compared to other markets.
    - Sales, Profit, and Shipping Cost distributions are right-skewed, meaning most transactions are small, with a few very large orders driving overall performance.
    - Profit has the highest number of outliers, indicating high variability in margins across orders.
    - The Technology category generates the highest profit, making it the most valuable category for the business.
    - The Furniture category has the highest average discount, which may impact profitability.
    - Some sub-categories (e.g., Tables) generate consistent losses despite sales activity.
    - Higher discounts are generally associated with lower profitability.
    - Eastern Africa has the highest return rate among regions.
    - Office Supplies also shows a high return rate compared to other categories.
    """)
    
    # Business Problems
    st.subheader("Business Problems")

    st.markdown("""
    - High discounts in certain categories (especially Furniture) are negatively impacting profit margins.
    - Some sub-categories are loss-making, indicating inefficient pricing or cost structures.
    - Profit variability is high, suggesting inconsistent pricing or discount strategies.
    - Certain regions (e.g., Eastern Africa) have high return rates, which may indicate quality, logistics, or customer satisfaction issues.
    - The business relies heavily on a small number of high-value orders, which increases revenue risk.
    """)
    # Recommendations
    st.subheader("Recommendations")

    st.markdown("""
    - Re-evaluate discount strategies, especially in low-margin categories like Furniture.
    - Focus on promoting and expanding Technology products, as they generate the highest profit.
    - Investigate and improve loss-making sub-categories (e.g., Tables) through pricing or cost optimization.
    - Analyze return patterns in high-return regions (e.g., Eastern Africa) to reduce returns and improve customer satisfaction.
    - Optimize shipping and operational costs to improve overall profitability.
    - Leverage high-performing markets like Asia Pacific for further business expansion.
    """)
st.markdown("""
<hr style="margin-top:10px; margin-bottom:10px;">
<p style="text-align:center; color:#64748b; font-size:14px;">
Built with Streamlit • Global Superstore Project 
</p>low_html=True)

""", unsafe_allow_html=True)
  

