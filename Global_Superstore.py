import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Global Superstore", layout="wide")

BG_IMAGE = "https://img.freepik.com/premium-photo/store-with-lot-cans-beer-shelf_939033-80225.jpg?semt=ais_hybrid&w=740&q=80"

# =========================
# Styling
# =========================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: #eef4fb;
}}

.block-container {{
    padding-top: 1.2rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    padding-bottom: 1.5rem;
    max-width: 100%;
}}

/* Hide sidebar completely */
section[data-testid="stSidebar"] {{
    display: none;
}}

/* Header */
.app-header {{
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(148, 163, 184, 0.35);
    border-radius: 24px;
    padding: 22px 28px;
    margin-bottom: 18px;
    box-shadow: 0 16px 45px rgba(15, 23, 42, 0.10);
    display: flex;
    justify-content: space-between;
    align-items: center;
    animation: fadeDown 0.65s ease both;
}}

.brand-title {{
    color: #0f172a;
    font-size: 24px;
    font-weight: 800;
    margin: 0;
}}

.brand-subtitle {{
    color: #64748b;
    font-size: 15px;
    margin-top: 5px;
}}

.brand-icon {{
    width: 46px;
    height: 46px;
    border-radius: 16px;
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    box-shadow: 0 12px 28px rgba(37, 99, 235, 0.35);
}}

.brand-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
}}

/* Top navigation radio */
div[role="radiogroup"] {{
    background: rgba(255,255,255,0.78);
    border: 1px solid rgba(148,163,184,0.35);
    border-radius: 999px;
    padding: 8px;
    width: fit-content;
    margin: 0 auto 20px auto;
    box-shadow: 0 12px 30px rgba(15,23,42,0.08);
}}

div[role="radiogroup"] label {{
    border-radius: 999px !important;
    padding: 10px 18px !important;
    margin-right: 4px !important;
    transition: all 0.25s ease;
}}

div[role="radiogroup"] label:hover {{
    background: rgba(37,99,235,0.10);
    transform: translateY(-1px);
}}

div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {{
    display: none;
}}

div[role="radiogroup"] label p {{
    font-weight: 700;
    font-size: 15px;
}}

/* Hero */
.hero {{
    min-height: 650px;
    border-radius: 30px;
    overflow: hidden;
    background-image:
        linear-gradient(90deg, rgba(5, 15, 35, 0.86) 0%, rgba(15, 23, 42, 0.68) 42%, rgba(15, 23, 42, 0.35) 100%),
        url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    box-shadow: 0 24px 70px rgba(15, 23, 42, 0.22);
    position: relative;
    animation: fadeUp 0.8s ease both;
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
    z-index: 1;
    padding: 90px 70px;
    max-width: 760px;
    color: white;
    animation: fadeUp 1s ease both;
}}

.hero-badge {{
    display: inline-block;
    padding: 9px 15px;
    border-radius: 999px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    margin-bottom: 20px;
    font-weight: 700;
}}

.hero h1 {{
    font-size: 58px;
    line-height: 1.05;
    font-weight: 800;
    margin: 0 0 20px 0;
    letter-spacing: -1.5px;
}}

.hero p {{
    font-size: 22px;
    line-height: 1.55;
    color: #e2e8f0;
    margin-bottom: 32px;
}}

.hero-button {{
    display: inline-block;
    background: linear-gradient(135deg, #2563eb, #0ea5e9);
    color: white;
    padding: 14px 22px;
    border-radius: 14px;
    font-weight: 800;
    box-shadow: 0 14px 34px rgba(37, 99, 235, 0.45);
}}

.hero-kpis {{
    position: absolute;
    z-index: 2;
    left: 70px;
    bottom: 65px;
    display: flex;
    gap: 22px;
    flex-wrap: wrap;
}}

.hero-kpi-card {{
    width: 250px;
    padding: 22px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.14);
    border: 1px solid rgba(255, 255, 255, 0.24);
    backdrop-filter: blur(13px);
    color: white;
    box-shadow: 0 20px 45px rgba(0,0,0,0.18);
    animation: fadeUp 1.05s ease both;
}}

.hero-kpi-value {{
    font-size: 28px;
    font-weight: 800;
}}

.hero-kpi-label {{
    color: #cbd5e1;
    font-weight: 600;
    margin-top: 6px;
}}

/* Page background for inner pages */
.page-shell {{
    border-radius: 30px;
    padding: 26px;
    background-image:
        linear-gradient(rgba(239, 246, 255, 0.82), rgba(239, 246, 255, 0.82)),
        url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    box-shadow: 0 22px 60px rgba(15, 23, 42, 0.13);
    animation: fadeUp 0.75s ease both;
}}

.page-title-card {{
    background: rgba(255, 255, 255, 0.82);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(148, 163, 184, 0.30);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.10);
}}

.page-title-card h2 {{
    margin: 0;
    color: #0f172a;
    font-size: 30px;
    font-weight: 800;
}}

.page-title-card p {{
    margin: 8px 0 0 0;
    color: #64748b;
    font-size: 16px;
}}

.filter-card {{
    background: rgba(255, 255, 255, 0.86);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(148, 163, 184, 0.32);
    border-radius: 22px;
    padding: 18px 20px;
    margin-bottom: 22px;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.09);
}}

.filter-title {{
    color: #0f172a;
    font-weight: 800;
    margin-bottom: 10px;
    font-size: 17px;
}}

.glass-card {{
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(148, 163, 184, 0.32);
    border-radius: 24px;
    padding: 22px;
    margin-bottom: 22px;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.10);
    transition: all 0.25s ease;
}}

.glass-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 24px 55px rgba(15, 23, 42, 0.14);
}}

.kpi-card {{
    background: rgba(255,255,255,0.90);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(148, 163, 184, 0.30);
    border-radius: 24px;
    padding: 24px;
    min-height: 128px;
    box-shadow: 0 18px 45px rgba(15,23,42,0.10);
    transition: all 0.25s ease;
}}

.kpi-card:hover {{
    transform: translateY(-5px);
}}

.kpi-value {{
    color: #0f172a;
    font-size: 30px;
    font-weight: 800;
}}

.kpi-label {{
    color: #64748b;
    font-weight: 700;
    margin-top: 8px;
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 10px;
    background: rgba(255,255,255,0.75);
    padding: 8px;
    border-radius: 18px;
    margin-bottom: 18px;
}}

.stTabs [data-baseweb="tab"] {{
    border-radius: 14px;
    padding: 10px 18px;
    font-weight: 700;
}}

.stTabs [aria-selected="true"] {{
    background: linear-gradient(135deg, #2563eb, #0ea5e9) !important;
    color: white !important;
}}

div[data-testid="stDataFrame"] {{
    border-radius: 18px;
    overflow: hidden;
}}

hr {{
    border: none;
    height: 1px;
    background: rgba(100,116,139,0.25);
    margin-top: 30px;
}}

.footer {{
    text-align: center;
    color: #64748b;
    font-weight: 600;
    padding: 12px;
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

# =========================
# Load Data
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("df_clean.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    return df

df = load_data()
df["month"] = df["order_date"].dt.to_period("M").astype(str)
df["year"] = df["order_date"].dt.year

# =========================
# Helpers
# =========================
def beautify_fig(fig):
    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="rgba(255,255,255,0.65)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=13, color="#334155"),
        title=dict(font=dict(size=21, color="#0f172a")),
        margin=dict(l=20, r=20, t=62, b=20),
    )
    fig.update_xaxes(showgrid=False, linecolor="#cbd5e1")
    fig.update_yaxes(showgrid=True, gridcolor="#e2e8f0", linecolor="#cbd5e1")
    return fig

def page_intro(title, subtitle):
    st.markdown(f"""
    <div class="page-title-card">
        <h2>{title}</h2>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def metric_card(value, label):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Header + Navigation
# =========================
st.markdown("""
<div class="app-header">
    <div class="brand-wrap">
        <div class="brand-icon">🛒</div>
        <div>
            <div class="brand-title">Global Superstore Analytics Dashboard</div>
            <div class="brand-subtitle">Interactive insights for smarter business decisions</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "",
    ["🏠 Home", "📊 Summary Dashboard", "🔎 Detailed Analysis", "💡 Insights & Recommendations"],
    horizontal=True,
    label_visibility="collapsed"
)

page_clean = page.split(" ", 1)[1]

# =========================
# Filters: ONLY Summary + Detailed
# =========================
filtered_df = df.copy()

if page_clean in ["Summary Dashboard", "Detailed Analysis"]:
    st.markdown('<div class="filter-card"><div class="filter-title">Filters</div>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns([2, 2, 2])

    with f1:
        selected_regions = st.multiselect(
            "Region",
            options=sorted(df["region"].dropna().unique()),
            default=sorted(df["region"].dropna().unique())
        )

    with f2:
        selected_markets = st.multiselect(
            "Market",
            options=sorted(df["market"].dropna().unique()),
            default=sorted(df["market"].dropna().unique())
        )

    with f3:
        min_year, max_year = int(df["year"].min()), int(df["year"].max())
        selected_years = st.slider("Years", min_year, max_year, (min_year, max_year))

    st.markdown("</div>", unsafe_allow_html=True)

    filtered_df = df[
        df["region"].isin(selected_regions)
        & df["market"].isin(selected_markets)
        & df["year"].between(selected_years[0], selected_years[1])
    ].copy()

# =========================
# Home
# =========================
if page_clean == "Home":
    total_sales = df["sales"].sum()
    total_profit = df["profit"].sum()
    total_orders = df["order_id"].nunique()

    st.markdown(f"""
    <div class="hero">
        <div class="hero-content">
            <div class="hero-badge">Modern Business Analytics</div>
            <h1>Global Superstore Dashboard</h1>
            <p>Analyze sales, profit, customers, and performance across regions and years with a clean executive-ready interface.</p>
            <div class="hero-button">Explore Dashboard →</div>
        </div>

        <div class="hero-kpis">
            <div class="hero-kpi-card">
                <div class="hero-kpi-value">${total_sales:,.0f}</div>
                <div class="hero-kpi-label">Total Sales</div>
            </div>
            <div class="hero-kpi-card">
                <div class="hero-kpi-value">${total_profit:,.0f}</div>
                <div class="hero-kpi-label">Total Profit</div>
            </div>
            <div class="hero-kpi-card">
                <div class="hero-kpi-value">{total_orders:,}</div>
                <div class="hero-kpi-label">Total Orders</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Summary Dashboard
# =========================
elif page_clean == "Summary Dashboard":
    st.markdown('<div class="page-shell">', unsafe_allow_html=True)
    page_intro("Summary Dashboard", "Executive overview of sales, profit, orders, and returns.")

    total_sales = filtered_df["sales"].sum()
    total_profit = filtered_df["profit"].sum()
    total_orders = filtered_df["order_id"].nunique()
    return_rate = (filtered_df["returned"] == "Yes").mean() if "returned" in filtered_df.columns else 0

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card(f"${total_sales:,.0f}", "Total Sales")
    with c2:
        metric_card(f"${total_profit:,.0f}", "Total Profit")
    with c3:
        metric_card(f"{total_orders:,}", "Total Orders")
    with c4:
        metric_card(f"{return_rate * 100:.1f}%", "Return Rate")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    sales_by_month = filtered_df.groupby("month")["sales"].sum().reset_index()
    fig = px.line(sales_by_month, x="month", y="sales", markers=True, title="Total Sales by Month")
    st.plotly_chart(beautify_fig(fig), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    sales_by_market = (
        filtered_df.groupby("market")["sales"]
        .sum()
        .reset_index()
        .sort_values(by="sales", ascending=False)
        .head(10)
    )
    fig2 = px.bar(sales_by_market, x="market", y="sales", title="Top 10 Markets by Revenue")
    st.plotly_chart(beautify_fig(fig2), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Detailed Analysis
# =========================
elif page_clean == "Detailed Analysis":
    st.markdown('<div class="page-shell">', unsafe_allow_html=True)
    page_intro("Detailed Analysis", "Deep dive into sales, profit, returns, customers, managers, and shipping.")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Sales",
        "Profit & Discount",
        "Returns",
        "Customers",
        "Managers",
        "Shipping"
    ])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        sales_by_year = filtered_df.groupby("year")["sales"].sum().reset_index()
        fig = px.line(sales_by_year, x="year", y="sales", markers=True, title="Total Sales by Year")
        fig.update_xaxes(tickmode="linear", dtick=1)
        st.plotly_chart(beautify_fig(fig), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            sales_by_category = filtered_df.groupby("category")["sales"].sum().reset_index().sort_values(by="sales", ascending=False)
            fig = px.bar(sales_by_category, x="category", y="sales", title="Sales by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            top_products = filtered_df.groupby("product_name")["sales"].sum().reset_index().sort_values(by="sales", ascending=False).head(10)
            fig = px.bar(top_products, x="product_name", y="sales", title="Top 10 Products by Revenue")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            cat_profit = filtered_df.groupby("category")["profit"].sum().reset_index().sort_values(by="profit", ascending=False)
            fig = px.bar(cat_profit, x="category", y="profit", title="Profit by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            cat_discount = filtered_df.groupby("category")["discount"].mean().reset_index().sort_values(by="discount", ascending=False)
            fig = px.bar(cat_discount, x="category", y="discount", title="Average Discount by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        loss_bysubcat = filtered_df[filtered_df["profit"] < 0].groupby("sub-category")["profit"].sum().reset_index().sort_values(by="profit")
        fig = px.bar(loss_bysubcat, x="sub-category", y="profit", title="Loss-Making Sub-Categories")
        st.plotly_chart(beautify_fig(fig), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            return_rate_by_region = filtered_df.groupby("region")["returned"].apply(lambda x: (x == "Yes").mean()).reset_index().sort_values(by="returned", ascending=False)
            fig = px.bar(return_rate_by_region, x="region", y="returned", title="Return Rate by Region")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            return_rate_by_category = filtered_df.groupby("category")["returned"].apply(lambda x: (x == "Yes").mean()).reset_index().sort_values(by="returned", ascending=False)
            fig = px.bar(return_rate_by_category, x="category", y="returned", title="Return Rate by Category")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            segment_sales = filtered_df.groupby("segment")["sales"].sum().reset_index().sort_values(by="sales", ascending=False)
            fig = px.bar(segment_sales, x="segment", y="sales", title="Sales by Customer Segment")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            most_active_person = (
                filtered_df.groupby(["region", "person"])["order_id"]
                .count()
                .reset_index(name="order_count")
                .sort_values(by=["region", "order_count"], ascending=[True, False])
            )
            most_active_person = most_active_person.groupby("region").head(1)
            fig = px.bar(most_active_person, x="person", y="order_count", title="Most Active Person by Region")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        avg_order_value = filtered_df.groupby("order_id")["sales"].sum().mean()
        metric_card(f"${avg_order_value:,.2f}", "Average Order Value")

    with tab5:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            sales_by_person = filtered_df.groupby("person")["sales"].sum().reset_index().sort_values(by="sales", ascending=False).head(10)
            fig = px.bar(sales_by_person, x="person", y="sales", title="Sales by Person")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            profit_by_person = filtered_df.groupby("person")["profit"].sum().reset_index().sort_values(by="profit", ascending=False).head(10)
            fig = px.bar(profit_by_person, x="person", y="profit", title="Profit by Person")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab6:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            fig = px.histogram(filtered_df, x="ship_mode", title="Shipping Mode Distribution")
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            shipping_by_year = filtered_df.groupby(filtered_df["ship_date"].dt.year)["shipping_cost"].sum().reset_index()
            shipping_by_year.columns = ["year", "shipping_cost"]
            fig = px.line(shipping_by_year, x="year", y="shipping_cost", markers=True, title="Total Shipping Cost by Year")
            fig.update_xaxes(tickmode="linear", dtick=1)
            st.plotly_chart(beautify_fig(fig), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        total_shipping_cost = filtered_df["shipping_cost"].sum()
        metric_card(f"${total_shipping_cost:,.2f}", "Total Shipping Cost")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Insights & Recommendations
# No filters here
# =========================
elif page_clean == "Insights & Recommendations":
    st.markdown('<div class="page-shell">', unsafe_allow_html=True)
    page_intro("Insights & Recommendations", "Final business findings organized in a clean decision table.")

    insights_data = [
        ["Insight", "Standard Class is the most commonly used shipping mode, indicating preference for low-cost delivery.", "Medium"],
        ["Insight", "Consumer segment is a key revenue driver and should remain a main business focus.", "High"],
        ["Insight", "Technology generates the highest profit and represents a strong growth opportunity.", "High"],
        ["Insight", "Asia Pacific shows strong sales presence compared to other markets.", "Medium"],
        ["Problem", "High discounts, especially in Furniture, can reduce profitability.", "High"],
        ["Problem", "Some sub-categories such as Tables generate losses despite sales activity.", "High"],
        ["Problem", "Eastern Africa has a high return rate, which may indicate logistics or satisfaction issues.", "High"],
        ["Recommendation", "Re-evaluate discount strategy in low-margin categories like Furniture.", "High"],
        ["Recommendation", "Promote Technology products because they generate the highest profit.", "High"],
        ["Recommendation", "Investigate loss-making sub-categories and optimize pricing or costs.", "High"],
        ["Recommendation", "Analyze return patterns in high-return regions and improve logistics quality.", "Medium"],
        ["Recommendation", "Leverage strong markets such as Asia Pacific for business expansion.", "Medium"],
    ]

    insights_df = pd.DataFrame(insights_data, columns=["Type", "Description", "Priority"])

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.dataframe(insights_df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Footer
# =========================
st.markdown("""
<hr>
<div class="footer">Built with Streamlit • Global Superstore Project</div>
""", unsafe_allow_html=True)

