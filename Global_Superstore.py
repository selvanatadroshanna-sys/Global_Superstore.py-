
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

BG_IMAGE = "https://img.freepik.com/premium-photo/store-with-lot-cans-beer-shelf_939033-80225.jpg?semt=ais_hybrid&w=740&q=80"

# =========================================================
# CSS
# =========================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: #eef4fb;
}}

.block-container {{
    padding-top: 1rem;
    padding-left: 2.3rem;
    padding-right: 2.3rem;
    padding-bottom: 1rem;
    max-width: 100%;
}}

section[data-testid="stSidebar"] {{
    display: none;
}}

/* ================= HEADER ================= */
.app-header {{
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(148,163,184,0.32);
    border-radius: 24px;
    padding: 20px 26px;
    margin-bottom: 16px;
    box-shadow: 0 14px 38px rgba(15,23,42,0.10);
    display: flex;
    align-items: center;
    gap: 14px;
    animation: fadeDown .55s ease both;
}}

.logo {{
    width: 48px;
    height: 48px;
    border-radius: 16px;
    background: linear-gradient(135deg,#2563eb,#0ea5e9);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    box-shadow: 0 12px 28px rgba(37,99,235,.30);
}}

.app-title {{
    font-size: 25px;
    font-weight: 900;
    color: #0f172a;
    margin: 0;
}}

.app-subtitle {{
    color: #64748b;
    margin-top: 4px;
    font-size: 15px;
    font-weight: 500;
}}

/* ================= TOP NAV ================= */
div[role="radiogroup"] {{
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(148,163,184,0.32);
    border-radius: 999px;
    padding: 8px;
    width: fit-content;
    margin: 0 auto 18px auto;
    box-shadow: 0 12px 30px rgba(15,23,42,0.08);
}}

div[role="radiogroup"] label {{
    border-radius: 999px !important;
    padding: 9px 18px !important;
    margin-right: 5px !important;
    transition: all .25s ease;
}}

div[role="radiogroup"] label:hover {{
    background: rgba(37,99,235,.10);
    transform: translateY(-1px);
}}

div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {{
    display: none;
}}

div[role="radiogroup"] label p {{
    font-weight: 800;
    font-size: 15px;
    color: #0f172a;
}}

/* ================= HOME HERO ================= */
.hero {{
    min-height: 650px;
    border-radius: 30px;
    overflow: hidden;
    background-image:
        linear-gradient(90deg, rgba(5,15,35,.88) 0%, rgba(15,23,42,.68) 45%, rgba(15,23,42,.32) 100%),
        url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    box-shadow: 0 24px 70px rgba(15,23,42,.22);
    position: relative;
    animation: fadeUp .75s ease both;
}}

.hero::after {{
    content: "";
    position: absolute;
    inset: 0;
    backdrop-filter: blur(2.5px);
    pointer-events: none;
}}

.hero-content {{
    position: relative;
    z-index: 2;
    padding: 82px 70px;
    max-width: 760px;
    color: white;
}}

.hero h1 {{
    font-size: 58px;
    line-height: 1.05;
    font-weight: 900;
    margin: 0 0 20px 0;
    letter-spacing: -1.5px;
}}

.hero p {{
    font-size: 22px;
    line-height: 1.55;
    color: #e2e8f0;
    margin-bottom: 28px;
}}

.hero-kpis {{
    position: absolute;
    z-index: 3;
    left: 70px;
    bottom: 60px;
    display: flex;
    gap: 22px;
    flex-wrap: wrap;
}}

.hero-kpi {{
    width: 255px;
    padding: 22px;
    border-radius: 20px;
    background: rgba(255,255,255,.14);
    border: 1px solid rgba(255,255,255,.24);
    backdrop-filter: blur(13px);
    color: white;
    box-shadow: 0 20px 45px rgba(0,0,0,.18);
}}

.hero-kpi-value {{
    font-size: 28px;
    font-weight: 900;
}}

.hero-kpi-label {{
    color: #cbd5e1;
    font-weight: 700;
    margin-top: 6px;
}}

/* Streamlit button as hero CTA */
div[data-testid="stButton"] > button {{
    background: linear-gradient(135deg,#2563eb,#0ea5e9);
    color: white;
    border: 0;
    border-radius: 16px;
    padding: 0.8rem 1.4rem;
    font-weight: 900;
    box-shadow: 0 14px 34px rgba(37,99,235,.38);
    transition: all .25s ease;
}}

div[data-testid="stButton"] > button:hover {{
    transform: translateY(-2px);
    color: white;
    box-shadow: 0 18px 42px rgba(37,99,235,.48);
}}

/* ================= INNER PAGES ================= */
.page-shell {{
    border-radius: 30px;
    padding: 24px;
    background-image:
        linear-gradient(rgba(239,246,255,.84), rgba(239,246,255,.84)),
        url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    box-shadow: 0 22px 60px rgba(15,23,42,.13);
    animation: fadeUp .7s ease both;
}}

.section-title {{
    background: rgba(255,255,255,.88);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(148,163,184,.28);
    border-radius: 22px;
    padding: 20px 22px;
    margin-bottom: 18px;
    box-shadow: 0 14px 35px rgba(15,23,42,.08);
}}

.section-title h2 {{
    color: #0f172a;
    font-size: 32px;
    font-weight: 900;
    margin: 0;
    letter-spacing: -0.6px;
}}

.section-title span {{
    color: #64748b;
    font-size: 15px;
    font-weight: 600;
}}

.custom-card {{
    background: rgba(255,255,255,.90);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(148,163,184,.28);
    border-radius: 22px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 14px 35px rgba(15,23,42,.09);
    transition: all .25s ease;
}}

.custom-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 20px 45px rgba(15,23,42,.12);
}}

.kpi-card {{
    background: rgba(255,255,255,.92);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(148,163,184,.28);
    border-radius: 22px;
    padding: 22px;
    min-height: 120px;
    box-shadow: 0 14px 35px rgba(15,23,42,.09);
    transition: all .25s ease;
}}

.kpi-card:hover {{
    transform: translateY(-4px);
}}

.kpi-value {{
    color: #0f172a;
    font-size: 30px;
    font-weight: 900;
}}

.kpi-label {{
    color: #64748b;
    font-weight: 800;
    margin-top: 8px;
}}

/* ================= FILTERS ================= */
.filter-card {{
    background: rgba(255,255,255,.92);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(148,163,184,.28);
    border-radius: 20px;
    padding: 14px 18px 10px 18px;
    margin-bottom: 18px;
    box-shadow: 0 12px 28px rgba(15,23,42,.08);
}}

.filter-title {{
    color: #0f172a;
    font-size: 28px;
    font-weight: 900;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}}

.filter-card label {{
    font-weight: 800 !important;
    color: #334155 !important;
    font-size: 14px !important;
}}

.filter-card [data-baseweb="select"] > div {{
    min-height: 42px !important;
    border-radius: 14px !important;
    background: #f8fafc !important;
    border-color: #dbe4ef !important;
}}

.filter-card .stSlider {{
    padding-top: 0 !important;
}}

/* ================= TABS ================= */
.stTabs [data-baseweb="tab-list"] {{
    gap: 10px;
    background: rgba(255,255,255,.78);
    padding: 8px;
    border-radius: 18px;
    margin-bottom: 18px;
}}

.stTabs [data-baseweb="tab"] {{
    border-radius: 14px;
    padding: 10px 18px;
    font-weight: 800;
}}

.stTabs [aria-selected="true"] {{
    background: linear-gradient(135deg,#2563eb,#0ea5e9) !important;
    color: white !important;
}}

/* ================= TABLE ================= */
.insights-table {{
    width: 100%;
    border-collapse: collapse;
    background: rgba(255,255,255,.95);
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 14px 35px rgba(15,23,42,.08);
}}

.insights-table th {{
    background: linear-gradient(135deg,#2563eb,#0ea5e9);
    color: white;
    padding: 14px 16px;
    text-align: left;
    font-size: 15px;
}}

.insights-table td {{
    padding: 14px 16px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
    font-size: 14px;
    line-height: 1.55;
}}

.insights-table tr:hover td {{
    background: #f8fafc;
}}

div[data-testid="stDataFrame"] {{
    border-radius: 18px;
    overflow: hidden;
}}

hr {{
    border: none;
    height: 1px;
    background: rgba(100,116,139,.25);
    margin-top: 26px;
}}

.footer {{
    text-align: center;
    color: #64748b;
    font-weight: 700;
    padding: 10px;
}}

@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(18px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

@keyframes fadeDown {{
    from {{ opacity: 0; transform: translateY(-12px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    df = pd.read_csv("df_clean.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    df["year"] = df["order_date"].dt.year
    return df

df = load_data()

# =========================================================
# HELPER FUNCTIONS
# =========================================================
def beautify_fig(fig):
    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="rgba(255,255,255,0.68)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=13, color="#334155"),
        title=dict(font=dict(size=22, color="#0f172a")),
        margin=dict(l=20, r=20, t=60, b=20),
    )
    fig.update_xaxes(showgrid=False, linecolor="#cbd5e1")
    fig.update_yaxes(showgrid=True, gridcolor="#e2e8f0", linecolor="#cbd5e1")
    return fig

def kpi_card(value, label):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def section_title(title, subtitle):
    st.markdown(f"""
    <div class="section-title">
        <h2>{title}</h2>
        <span>{subtitle}</span>
    </div>
    """, unsafe_allow_html=True)

def open_card():
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

def close_card():
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# SESSION STATE FOR NAVIGATION
# =========================================================
pages = ["Home", "Summary Dashboard", "Detailed Analysis", "Insights & Recommendations"]

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="app-header">
    <div class="logo">🛒</div>
    <div>
        <div class="app-title">Global Superstore Analytics Dashboard</div>
        <div class="app-subtitle">Interactive insights for smarter business decisions</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# NAVIGATION
# =========================================================
default_index = pages.index(st.session_state.selected_page)

page = st.radio(
    "",
    pages,
    index=default_index,
    horizontal=True,
    label_visibility="collapsed"
)

st.session_state.selected_page = page

# =========================================================
# FILTERS ONLY IN SUMMARY + DETAILED
# =========================================================
filtered_df = df.copy()

if page in ["Summary Dashboard", "Detailed Analysis"]:
    st.markdown('<div class="filter-card"><div class="filter-title">Filters</div>', unsafe_allow_html=True)

    f1, f2, f3 = st.columns([1.2, 1.2, 1.6])

    region_options = ["All Regions"] + sorted(df["region"].dropna().unique().tolist())
    market_options = ["All Markets"] + sorted(df["market"].dropna().unique().tolist())

    with f1:
        selected_region = st.selectbox("Region", options=region_options, index=0)

    with f2:
        selected_market = st.selectbox("Market", options=market_options, index=0)

    with f3:
        min_year, max_year = int(df["year"].min()), int(df["year"].max())
        selected_years = st.slider("Years", min_year, max_year, (min_year, max_year))

    st.markdown("</div>", unsafe_allow_html=True)

    filtered_df = df.copy()

    if selected_region != "All Regions":
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    if selected_market != "All Markets":
        filtered_df = filtered_df[filtered_df["market"] == selected_market]

    filtered_df = filtered_df[
        filtered_df["year"].between(selected_years[0], selected_years[1])
    ].copy()

# =========================================================
# HOME PAGE
# =========================================================
if page == "Home":
    total_sales = df["sales"].sum()
    total_profit = df["profit"].sum()
    total_orders = df["order_id"].nunique()

    st.markdown(f"""
    <div class="hero">
        <div class="hero-content">
            <h1>Global Superstore Dashboard</h1>
            <p>Analyze sales, profit, customers, and performance across regions and years through a clean professional dashboard.</p>
        </div>

        <div class="hero-kpis">
            <div class="hero-kpi">
                <div class="hero-kpi-value">${total_sales:,.0f}</div>
                <div class="hero-kpi-label">Total Sales</div>
            </div>
            <div class="hero-kpi">
                <div class="hero-kpi-value">${total_profit:,.0f}</div>
                <div class="hero-kpi-label">Total Profit</div>
            </div>
            <div class="hero-kpi">
                <div class="hero-kpi-value">{total_orders:,}</div>
                <div class="hero-kpi-label">Total Orders</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("Explore Dashboard →"):
        st.session_state.selected_page = "Summary Dashboard"
        st.rerun()

# =========================================================
# SUMMARY DASHBOARD
# =========================================================
elif page == "Summary Dashboard":
    st.markdown('<div class="page-shell">', unsafe_allow_html=True)

    section_title("Summary Dashboard", "Executive overview of sales, profit, orders, and returns.")

    total_sales = filtered_df["sales"].sum()
    total_profit = filtered_df["profit"].sum()
    total_orders = filtered_df["order_id"].nunique()
    return_rate = (filtered_df["returned"] == "Yes").mean() if "returned" in filtered_df.columns else 0

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        kpi_card(f"${total_sales:,.0f}", "Total Sales")
    with c2:
        kpi_card(f"${total_profit:,.0f}", "Total Profit")
    with c3:
        kpi_card(f"{total_orders:,}", "Total Orders")
    with c4:
        kpi_card(f"{return_rate * 100:.1f}%", "Return Rate")

    open_card()
    sales_by_month = filtered_df.groupby("month")["sales"].sum().reset_index()
    fig = px.line(sales_by_month, x="month", y="sales", markers=True, title="Total Sales by Month")
    st.plotly_chart(beautify_fig(fig), use_container_width=True)
    close_card()

    open_card()
    sales_by_market = (
        filtered_df.groupby("market")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
        .head(10)
    )
    fig2 = px.bar(sales_by_market, x="market", y="sales", title="Top 10 Markets by Revenue")
    st.plotly_chart(beautify_fig(fig2), use_container_width=True)
    close_card()

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# DETAILED ANALYSIS
# =========================================================
elif page == "Detailed Analysis":
    st.markdown('<div class="page-shell">', unsafe_allow_html=True)

    section_title("Detailed Analysis", "Deep dive into sales, profit, returns, customers, managers, and shipping.")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Sales",
        "Profit & Discount",
        "Returns",
        "Customers",
        "Managers",
        "Shipping"
    ])

    with tab1:
        open_card()
        sales_by_year = filtered_df.groupby("year")["sales"].sum().reset_index()
        fig = px.line(sales_by_year, x="year", y="sales", markers=True, title="Total Sales by Year")
        fig.update_xaxes(tickmode="linear", dtick=1)
        st.plotly_chart(beautify_fig(fig), use_container_width=True)
        close_card()

        col1, col2 = st.columns(2)

        with col1:
            open_card()
            sales_by_category = (
                filtered_df.groupby("category")["sales"]
                .sum()
                .reset_index()
                .sort_values(by="sales", ascending=False)
            )
            fig = px.bar(sales_by_category, x="category", y="sales", title="Sales by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        with col2:
            open_card()
            top_products = (
                filtered_df.groupby("product_name")["sales"]
                .sum()
                .reset_index()
                .sort_values(by="sales", ascending=False)
                .head(10)
            )
            fig = px.bar(top_products, x="product_name", y="sales", title="Top 10 Products by Revenue")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            open_card()
            cat_profit = (
                filtered_df.groupby("category")["profit"]
                .sum()
                .reset_index()
                .sort_values(by="profit", ascending=False)
            )
            fig = px.bar(cat_profit, x="category", y="profit", title="Profit by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        with col2:
            open_card()
            cat_discount = (
                filtered_df.groupby("category")["discount"]
                .mean()
                .reset_index()
                .sort_values(by="discount", ascending=False)
            )
            fig = px.bar(cat_discount, x="category", y="discount", title="Average Discount by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        open_card()
        loss_bysubcat = (
            filtered_df[filtered_df["profit"] < 0]
            .groupby("sub-category")["profit"]
            .sum()
            .reset_index()
            .sort_values(by="profit")
        )
        fig = px.bar(loss_bysubcat, x="sub-category", y="profit", title="Loss-Making Sub-Categories")
        st.plotly_chart(beautify_fig(fig), use_container_width=True)
        close_card()

    with tab3:
        col1, col2 = st.columns(2)

        with col1:
            open_card()
            return_rate_by_region = (
                filtered_df.groupby("region")["returned"]
                .apply(lambda x: (x == "Yes").mean())
                .reset_index()
                .sort_values(by="returned", ascending=False)
            )
            fig = px.bar(return_rate_by_region, x="region", y="returned", title="Return Rate by Region")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        with col2:
            open_card()
            return_rate_by_category = (
                filtered_df.groupby("category")["returned"]
                .apply(lambda x: (x == "Yes").mean())
                .reset_index()
                .sort_values(by="returned", ascending=False)
            )
            fig = px.bar(return_rate_by_category, x="category", y="returned", title="Return Rate by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

    with tab4:
        col1, col2 = st.columns(2)

        with col1:
            open_card()
            segment_sales = (
                filtered_df.groupby("segment")["sales"]
                .sum()
                .reset_index()
                .sort_values(by="sales", ascending=False)
            )
            fig = px.bar(segment_sales, x="segment", y="sales", title="Sales by Customer Segment")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        with col2:
            open_card()
            most_active_person = (
                filtered_df.groupby(["region", "person"])["order_id"]
                .count()
                .reset_index(name="order_count")
                .sort_values(by=["region", "order_count"], ascending=[True, False])
            )
            most_active_person = most_active_person.groupby("region").head(1)
            fig = px.bar(most_active_person, x="person", y="order_count", title="Most Active Person by Region")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        avg_order_value = filtered_df.groupby("order_id")["sales"].sum().mean()
        kpi_card(f"${avg_order_value:,.2f}", "Average Order Value")

    with tab5:
        col1, col2 = st.columns(2)

        with col1:
            open_card()
            sales_by_person = (
                filtered_df.groupby("person")["sales"]
                .sum()
                .reset_index()
                .sort_values(by="sales", ascending=False)
                .head(10)
            )
            fig = px.bar(sales_by_person, x="person", y="sales", title="Sales by Person")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        with col2:
            open_card()
            profit_by_person = (
                filtered_df.groupby("person")["profit"]
                .sum()
                .reset_index()
                .sort_values(by="profit", ascending=False)
                .head(10)
            )
            fig = px.bar(profit_by_person, x="person", y="profit", title="Profit by Person")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

    with tab6:
        col1, col2 = st.columns(2)

        with col1:
            open_card()
            fig = px.histogram(filtered_df, x="ship_mode", title="Shipping Mode Distribution")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        with col2:
            open_card()
            shipping_by_year = (
                filtered_df.groupby(filtered_df["ship_date"].dt.year)["shipping_cost"]
                .sum()
                .reset_index()
            )
            shipping_by_year.columns = ["year", "shipping_cost"]
            fig = px.line(shipping_by_year, x="year", y="shipping_cost", markers=True, title="Total Shipping Cost by Year")
            fig.update_xaxes(tickmode="linear", dtick=1)
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            close_card()

        total_shipping_cost = filtered_df["shipping_cost"].sum()
        kpi_card(f"${total_shipping_cost:,.2f}", "Total Shipping Cost")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# INSIGHTS & RECOMMENDATIONS
# =========================================================
elif page == "Insights & Recommendations":
    st.markdown('<div class="page-shell">', unsafe_allow_html=True)

    section_title("Insights & Recommendations", "Actionable business table.")

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

    st.markdown(
        insights_df.to_html(index=False, classes="insights-table", escape=False),
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<hr>
<div class="footer">Built with Streamlit • Global Superstore Project</div>
""", unsafe_allow_html=True)

