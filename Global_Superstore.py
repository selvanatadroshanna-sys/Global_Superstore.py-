import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(page_title='Global_Superstore',layout='wide')
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
:root { --navy: #0f172a; --blue: #2563eb; --muted: #64748b; --line: #e2e8f0; --card: rgba(255,255,255,0.92); }
html, body, [class*="css"] { font-family: 'Inter', Arial, sans-serif; }
.stApp { background: radial-gradient(circle at top left, rgba(37,99,235,0.14), transparent 32%), linear-gradient(135deg, #f8fbff 0%, #eef4ff 100%); }
.block-container { padding-top: 1.25rem; padding-bottom: 2rem; max-width: 1280px; }
section[data-testid="stSidebar"] { display: none; }
.app-header { background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 58%, #2563eb 100%); color: white; padding: 26px 30px; border-radius: 26px; box-shadow: 0 18px 45px rgba(15,23,42,0.22); margin-bottom: 18px; }
.app-header h1 { color: white; font-size: 34px; margin: 0 0 8px 0; letter-spacing: -0.6px; }
.app-header p { color: #dbeafe; margin: 0; font-size: 16px; }
div[data-testid="stRadio"] > label { display: none; }
div[role="radiogroup"] { display: flex; gap: 10px; flex-wrap: wrap; background: rgba(255,255,255,0.86); backdrop-filter: blur(12px); padding: 10px; border-radius: 22px; border: 1px solid var(--line); box-shadow: 0 12px 32px rgba(15,23,42,0.10); margin-bottom: 22px; }
div[role="radiogroup"] label { border-radius: 16px !important; padding: 11px 18px !important; background: transparent; border: 1px solid transparent; color: var(--navy) !important; font-weight: 700; transition: all 0.2s ease; }
div[role="radiogroup"] label:hover { background: #eff6ff; border-color: #bfdbfe; }
div[role="radiogroup"] label[data-checked="true"] { background: linear-gradient(90deg, #2563eb, #1d4ed8) !important; color: white !important; box-shadow: 0 10px 20px rgba(37,99,235,0.25); }
.page-card, .custom-card { background: var(--card); padding: 22px; border-radius: 24px; border: 1px solid var(--line); box-shadow: 0 12px 32px rgba(15,23,42,0.08); margin-bottom: 22px; }
.section-title { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
.section-title h2, .section-title h3 { margin: 0; color: var(--navy); }
.section-title span { color: var(--muted); font-size: 14px; }
.hero { position: relative; min-height: 520px; border-radius: 30px; overflow: hidden; background-image: linear-gradient(90deg, rgba(15,23,42,0.78), rgba(15,23,42,0.35)), url("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1600&q=80"); background-size: cover; background-position: center; box-shadow: 0 22px 55px rgba(15,23,42,0.20); border: 1px solid rgba(255,255,255,0.24); }
.hero-content { position: absolute; left: 42px; bottom: 42px; max-width: 660px; color: white; }
.hero-badge { display: inline-block; background: rgba(255,255,255,0.16); border: 1px solid rgba(255,255,255,0.28); padding: 8px 13px; border-radius: 999px; color: #dbeafe; font-weight: 700; margin-bottom: 18px; }
.hero h1 { color: white; font-size: 58px; line-height: 1.02; margin: 0 0 16px 0; letter-spacing: -1.4px; }
.hero p { color: #e0f2fe; font-size: 18px; line-height: 1.6; margin-bottom: 24px; }
.hero-stats { display: flex; gap: 12px; flex-wrap: wrap; }
.hero-stat { background: rgba(255,255,255,0.13); border: 1px solid rgba(255,255,255,0.24); border-radius: 18px; padding: 14px 18px; min-width: 135px; }
.hero-stat strong { display: block; font-size: 22px; color: white; }
.hero-stat small { color: #cbd5e1; }
.kpi-card { background: white; padding: 22px; border-radius: 22px; box-shadow: 0 12px 32px rgba(15,23,42,0.08); border: 1px solid var(--line); text-align: left; }
.kpi-title { font-size: 14px; color: var(--muted); margin-bottom: 10px; font-weight: 700; }
.kpi-value { font-size: 30px; font-weight: 800; color: var(--navy); }
.stTabs [data-baseweb="tab-list"] { gap: 10px; }
.stTabs [data-baseweb="tab"] { background: white; border: 1px solid var(--line); border-radius: 14px; padding: 10px 18px; font-weight: 700; }
.stTabs [aria-selected="true"] { background: #2563eb !important; color: white !important; }
div[data-testid="metric-container"] { background: white; border: 1px solid var(--line); padding: 16px; border-radius: 18px; box-shadow: 0 8px 22px rgba(15,23,42,0.07); }
.insights-table { width: 100%; border-collapse: separate; border-spacing: 0 12px; }
.insights-table th { background: #0f172a; color: white; padding: 15px; text-align: left; font-size: 14px; }
.insights-table td { background: white; padding: 15px; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); vertical-align: top; color: #334155; }
.insights-table td:first-child, .insights-table th:first-child { border-radius: 16px 0 0 16px; font-weight: 800; color: #1d4ed8; }
.insights-table td:last-child, .insights-table th:last-child { border-radius: 0 16px 16px 0; }
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

st.markdown("""
<div class="app-header">
    <h1>Global Superstore Analytics Dashboard</h1>
    <p>Professional analytics experience for sales, profit, returns, customers, and shipping performance.</p>
</div>
""", unsafe_allow_html=True)

# Top Navigation
page = st.radio(
    "Navigation",
    [
        "Home",
        "Summary Dashboard",
        "Detailed Analysis",
        "Insights & Recommendations"
    ],
    horizontal=True
)

# No top filters requested - use the full dataset across all pages
filtered_df = df.copy()

if page == "Home":
    total_sales_home = filtered_df["sales"].sum()
    total_profit_home = filtered_df["profit"].sum()
    total_orders_home = filtered_df["order_id"].nunique()

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-content">
                <div class="hero-badge">Executive Dashboard</div>
                <h1>Global Superstore Dashboard</h1>
                <p>Explore business performance across sales, profitability, customer behavior, returns, and logistics through a clean professional reporting interface.</p>
                <div class="hero-stats">
                    <div class="hero-stat"><strong>${total_sales_home:,.0f}</strong><small>Total Sales</small></div>
                    <div class="hero-stat"><strong>${total_profit_home:,.0f}</strong><small>Total Profit</small></div>
                    <div class="hero-stat"><strong>{total_orders_home:,}</strong><small>Total Orders</small></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="page-card">
        <div class="section-title">
            <h3>What this dashboard covers</h3>
            <span>Sales • Profit • Customers • Shipping • Returns</span>
        </div>
        <p style="color:#475569; line-height:1.7; margin-bottom:0;">
            Use the top navigation to move between the executive summary, detailed analysis, and the final recommendations table.
            The layout is clean with no filters on the Home page, keeping the first screen focused and presentation-ready.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 1. Summary Dashboard for Top Management

elif page == "Summary Dashboard":
    st.markdown('<div class="section-title"><h2>Summary Dashboard</h2><span>Executive overview</span></div>', unsafe_allow_html=True)

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
    st.markdown('<div class="section-title"><h2>Detailed Analysis</h2><span>Drill-down views</span></div>', unsafe_allow_html=True)

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
    st.markdown('<div class="section-title"><h2>Insights & Recommendations</h2><span>Actionable business table</span></div>', unsafe_allow_html=True)

    insights_data = [
        ["Shipping", "Standard Class is the most commonly used shipping mode, indicating a strong preference for low-cost delivery.", "Optimize Standard Class operations and negotiate better shipping rates to reduce cost."],
        ["Customer Segment", "The Consumer segment is the dominant and most profitable segment, making it the primary revenue driver.", "Prioritize Consumer-focused campaigns and loyalty offers."],
        ["Category Demand", "Office Supplies is the most frequent category, showing consistent and recurring demand.", "Maintain strong stock availability for recurring Office Supplies demand."],
        ["Sub-Category Demand", "Binders is one of the most popular sub-categories in terms of order frequency.", "Bundle Binders with related Office Supplies products to increase order value."],
        ["Market Performance", "The Asia Pacific market shows strong sales presence compared to other markets.", "Leverage Asia Pacific performance for further business expansion."],
        ["Sales Distribution", "Sales, Profit, and Shipping Cost are right-skewed, meaning a few large orders drive overall performance.", "Reduce dependency on large orders by increasing repeat purchases and mid-value orders."],
        ["Profit Variability", "Profit has many outliers, indicating high variability in margins across orders.", "Review pricing and discount rules to make margins more consistent."],
        ["Top Profit Category", "Technology generates the highest profit, making it the most valuable category.", "Promote Technology products and expand high-margin Technology offerings."],
        ["Discount Risk", "Furniture has the highest average discount, which may reduce profitability.", "Re-evaluate Furniture discounts and set minimum margin thresholds."],
        ["Loss-Making Areas", "Some sub-categories such as Tables generate consistent losses despite sales activity.", "Improve Tables pricing, reduce costs, or limit aggressive discounts."],
        ["Discount vs Profit", "Higher discounts are generally associated with lower profitability.", "Use targeted discounts only where they improve volume without damaging margin."],
        ["Returns", "Eastern Africa has the highest return rate among regions.", "Investigate quality, logistics, and customer satisfaction issues in high-return regions."],
        ["Category Returns", "Office Supplies also shows a high return rate compared to other categories.", "Analyze Office Supplies return reasons and improve product descriptions or quality checks."],
    ]

    insights_df = pd.DataFrame(
        insights_data,
        columns=["Area", "Insight / Problem", "Recommendation"]
    )

    st.markdown("""
    <div class="custom-card">
        <h3 style="margin-top:0;">Insights, Business Problems & Recommendations</h3>
        <p style="color:#64748b; margin-bottom:16px;">
            A structured summary of the main findings and recommended actions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        insights_df.to_html(index=False, classes="insights-table", escape=False),
        unsafe_allow_html=True
    )

st.markdown("""
<hr style="margin-top:10px; margin-bottom:10px;">
<p style="text-align:center; color:#64748b; font-size:14px;">
Built with Streamlit • Global Superstore Project 
</p>
""", unsafe_allow_html=True)
