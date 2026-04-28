
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="🛒",
    layout="wide"
)

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
    background:
        radial-gradient(circle at top left, rgba(59,130,246,0.10), transparent 32%),
        linear-gradient(135deg, #eef4fb 0%, #f8fbff 100%);
}}

.block-container {{
    padding-top: 1rem;
    padding-left: 2.2rem;
    padding-right: 2.2rem;
    padding-bottom: 1.2rem;
    max-width: 100%;
}}

section[data-testid="stSidebar"] {{
    display: none;
}}

/* Hide radio circles */
div[role="radiogroup"] label > div:first-child {{
    display: none !important;
}}

/* ================= TOP HEADER ================= */
.top-header {{
    background: rgba(255,255,255,0.92);
    border: 1px solid rgba(148,163,184,0.30);
    border-radius: 24px;
    padding: 18px 24px;
    margin-bottom: 14px;
    box-shadow: 0 18px 45px rgba(15,23,42,0.08);
    backdrop-filter: blur(18px);
    display: flex;
    align-items: center;
    gap: 14px;
}}

.logo-box {{
    width: 50px;
    height: 50px;
    border-radius: 17px;
    background: linear-gradient(135deg, #2563eb, #0ea5e9);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    box-shadow: 0 14px 32px rgba(37,99,235,0.30);
}}

.header-title {{
    color: #0f172a;
    font-size: 25px;
    font-weight: 900;
    letter-spacing: -0.4px;
    margin: 0;
}}

.header-subtitle {{
    color: #64748b;
    font-size: 15px;
    font-weight: 600;
    margin-top: 3px;
}}

/* ================= NAVIGATION ================= */
div[role="radiogroup"] {{
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(148,163,184,0.30);
    border-radius: 999px;
    padding: 8px;
    width: fit-content;
    margin: 0 auto 18px auto;
    box-shadow: 0 14px 34px rgba(15,23,42,0.08);
}}

div[role="radiogroup"] label {{
    border-radius: 999px !important;
    padding: 10px 18px !important;
    margin-right: 4px !important;
    transition: all 0.22s ease;
}}

div[role="radiogroup"] label:hover {{
    background: rgba(37,99,235,0.10);
    transform: translateY(-1px);
}}

div[role="radiogroup"] label p {{
    color: #0f172a;
    font-weight: 800;
    font-size: 15px;
}}

/* ================= HOME ================= */
.hero {{
    min-height: 430px;
    border-radius: 30px;
    position: relative;
    overflow: hidden;
    background-image:
        linear-gradient(90deg, rgba(2,6,23,0.88) 0%, rgba(15,23,42,0.72) 42%, rgba(15,23,42,0.35) 100%),
        url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    box-shadow: 0 28px 75px rgba(15,23,42,0.22);
    animation: fadeUp 0.7s ease both;
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
    padding: 76px 70px 70px 70px;
    max-width: 760px;
    color: white;
}}

.hero-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 999px;
    padding: 9px 15px;
    color: #e2e8f0;
    font-weight: 800;
    margin-bottom: 20px;
    backdrop-filter: blur(12px);
}}

.hero h1 {{
    font-size: 58px;
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -1.5px;
    margin: 0 0 18px 0;
}}

.hero p {{
    color: #e2e8f0;
    font-size: 21px;
    line-height: 1.55;
    margin: 0;
}}









.project-card {{
    margin-top: 20px;
    background: rgba(255,255,255,0.92);
    border: 1px solid rgba(148,163,184,0.28);
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 16px 42px rgba(15,23,42,0.08);
}}

.project-card h2 {{
    color: #0f172a;
    font-size: 26px;
    font-weight: 900;
    margin: 0 0 8px 0;
}}

.project-card p {{
    color: #475569;
    font-size: 16px;
    line-height: 1.7;
    margin: 0 0 14px 0;
}}

.feature-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-top: 16px;
}}

.feature-pill {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 13px;
    color: #334155;
    font-weight: 800;
    font-size: 14px;
}}

/* ================= COMMON COMPONENTS ================= */
.page-shell {{
    border-radius: 30px;
    padding: 24px;
    background-image:
        linear-gradient(rgba(248,251,255,0.90), rgba(248,251,255,0.90)),
        url("{BG_IMAGE}");
    background-size: cover;
    background-position: center;
    box-shadow: 0 24px 65px rgba(15,23,42,0.12);
    animation: fadeUp 0.65s ease both;
}}

.section-title {{
    background: rgba(255,255,255,0.90);
    border: 1px solid rgba(148,163,184,0.28);
    border-radius: 24px;
    padding: 20px 22px;
    margin-bottom: 18px;
    box-shadow: 0 14px 34px rgba(15,23,42,0.07);
    backdrop-filter: blur(16px);
}}

.section-title h2 {{
    color: #0f172a;
    font-size: 32px;
    font-weight: 900;
    letter-spacing: -0.7px;
    margin: 0;
}}

.section-title span {{
    color: #64748b;
    font-size: 15px;
    font-weight: 700;
}}

.chart-title {{
    color: #0f172a;
    font-size: 19px;
    font-weight: 900;
    margin: 8px 0 10px 0;
}}

.kpi-card {{
    background: rgba(255,255,255,0.94);
    border: 1px solid rgba(148,163,184,0.26);
    border-radius: 24px;
    padding: 22px;
    min-height: 118px;
    box-shadow: 0 16px 36px rgba(15,23,42,0.08);
    transition: all 0.22s ease;
}}

.kpi-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 22px 46px rgba(15,23,42,0.11);
}}

.kpi-value {{
    color: #0f172a;
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -0.6px;
}}

.kpi-label {{
    color: #64748b;
    font-size: 14px;
    font-weight: 800;
    margin-top: 7px;
}}

/* Streamlit containers */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    border-radius: 24px !important;
    border: 1px solid rgba(148,163,184,0.28) !important;
    box-shadow: 0 16px 36px rgba(15,23,42,0.08) !important;
    background: rgba(255,255,255,0.92) !important;
}}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
    box-shadow: 0 20px 44px rgba(15,23,42,0.11) !important;
}}

/* ================= FILTERS ================= */
.filter-panel {{
    background: rgba(255,255,255,0.94);
    border: 1px solid rgba(148,163,184,0.28);
    border-radius: 24px;
    padding: 16px 18px 12px 18px;
    margin-bottom: 18px;
    box-shadow: 0 14px 34px rgba(15,23,42,0.08);
    backdrop-filter: blur(16px);
}}

.filter-heading {{
    color: #0f172a;
    font-size: 25px;
    font-weight: 900;
    margin-bottom: 8px;
}}

.filter-panel label {{
    color: #334155 !important;
    font-size: 13px !important;
    font-weight: 900 !important;
}}

.filter-panel [data-baseweb="select"] > div {{
    min-height: 42px !important;
    border-radius: 14px !important;
    background: #f8fafc !important;
    border: 1px solid #dbe4ef !important;
}}

.filter-panel [data-baseweb="select"] span {{
    font-size: 14px !important;
    font-weight: 700 !important;
}}

.filter-panel .stSlider {{
    padding-top: 0 !important;
}}

.stSlider [data-baseweb="slider"] {{
    margin-top: 0 !important;
}}

/* ================= TABS ================= */
.stTabs [data-baseweb="tab-list"] {{
    gap: 8px;
    background: rgba(255,255,255,0.86);
    border: 1px solid rgba(148,163,184,0.24);
    border-radius: 20px;
    padding: 8px;
    margin-bottom: 18px;
}}

.stTabs [data-baseweb="tab"] {{
    border-radius: 14px;
    padding: 10px 17px;
    font-weight: 900;
}}

.stTabs [aria-selected="true"] {{
    background: linear-gradient(135deg,#2563eb,#0ea5e9) !important;
    color: white !important;
}}

/* ================= BUTTON ================= */
div[data-testid="stButton"] > button {{
    background: linear-gradient(135deg,#2563eb,#0ea5e9);
    color: white;
    border: 0;
    border-radius: 16px;
    padding: 0.78rem 1.4rem;
    font-weight: 900;
    box-shadow: 0 14px 34px rgba(37,99,235,0.36);
    transition: all 0.22s ease;
}}

div[data-testid="stButton"] > button:hover {{
    transform: translateY(-2px);
    color: white;
    box-shadow: 0 18px 42px rgba(37,99,235,0.46);
}}

/* ================= INSIGHTS TABLE ================= */
.insights-table {{
    width: 100%;
    border-collapse: collapse;
    background: rgba(255,255,255,0.96);
    border-radius: 22px;
    overflow: hidden;
    box-shadow: 0 16px 40px rgba(15,23,42,0.08);
}}

.insights-table th {{
    background: linear-gradient(135deg,#1d4ed8,#0ea5e9);
    color: white;
    padding: 15px 17px;
    text-align: left;
    font-size: 15px;
}}

.insights-table td {{
    padding: 15px 17px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
    font-size: 14px;
    line-height: 1.55;
    vertical-align: top;
}}

.insights-table tr:hover td {{
    background: #f8fafc;
}}

.footer {{
    text-align: center;
    color: #64748b;
    font-weight: 700;
    padding: 14px 0 4px 0;
}}

hr {{
    border: none;
    height: 1px;
    background: rgba(100,116,139,0.24);
    margin-top: 24px;
}}

@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(16px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

/* ================= SIMPLE PAGE TRANSITION ================= */
.main .block-container {{
    animation: pageFade 0.55s ease both;
}}

.page-shell,
.hero,
.project-card,
.filter-panel,
.top-header {{
    animation: pageFade 0.55s ease both;
}}

@keyframes pageFade {{
    from {{
        opacity: 0;
        transform: translateY(10px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

/* ================= FLOATING FILTER ================= */
.filter-panel {{
    position: sticky;
    top: 12px;
    z-index: 50;
    transition: all 0.25s ease;
}}

.filter-panel:hover {{
    transform: translateY(-2px);
    box-shadow: 0 22px 48px rgba(15,23,42,0.14);
}}

/* ================= STRONGER BUT SIMPLE HOVER ================= */
.kpi-card,
.project-card,
div[data-testid="stVerticalBlockBorderWrapper"] {{
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}}

.kpi-card:hover,
.project-card:hover,
div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
    transform: translateY(-5px);
    border-color: rgba(37,99,235,0.35) !important;
    box-shadow: 0 26px 55px rgba(15,23,42,0.15) !important;
}}

div[role="radiogroup"] label:hover,
.stTabs [data-baseweb="tab"]:hover {{
    transform: translateY(-2px);
}}

/* make filter look like Power BI floating bar */
.filter-panel {{
    max-width: 100%;
    margin-left: auto;
    margin-right: auto;
    border-left: 5px solid #2563eb;
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# =========================================================
@st.cache_data
def load_data(file_path: str = "df_clean.csv") -> pd.DataFrame:
    """Load and prepare the Global Superstore dataset."""
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("Dataset file not found. Please place `df_clean.csv` in the same folder as this app.")
        st.stop()

    data.columns = (
        data.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )

    required_columns = {
        "order_date", "ship_date", "sales", "profit", "order_id",
        "region", "market", "category", "discount", "shipping_cost"
    }
    missing_columns = sorted(required_columns - set(data.columns))
    if missing_columns:
        st.error(f"Missing required columns: {', '.join(missing_columns)}")
        st.stop()

    data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")
    data["ship_date"] = pd.to_datetime(data["ship_date"], errors="coerce")
    data = data.dropna(subset=["order_date", "ship_date"])

    data["month"] = data["order_date"].dt.to_period("M").astype(str)
    data["year"] = data["order_date"].dt.year
    return data

df = load_data()

# =========================================================
# HELPERS
# =========================================================
def beautify_fig(fig):
    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="rgba(255,255,255,0)",
        paper_bgcolor="rgba(255,255,255,0)",
        font=dict(family="Inter", size=13, color="#334155"),
        title=dict(font=dict(size=21, color="#0f172a"), x=0.02),
        margin=dict(l=20, r=20, t=58, b=25),
        hovermode="x unified",
    )
    fig.update_xaxes(showgrid=False, linecolor="#dbe4ef", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#e2e8f0", linecolor="#dbe4ef", zeroline=False)
    return fig

def kpi_card(value, label):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-value">{value}</div>
            <div class="kpi-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def section_title(title, subtitle):
    st.markdown(
        f"""
        <div class="section-title">
            <h2>{title}</h2>
            <span>{subtitle}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

def plot_in_card(fig):
    with st.container(border=True):
        st.plotly_chart(beautify_fig(fig), use_container_width=True)

def safe_bar_message(column_name):
    st.info(f"Column `{column_name}` is not available in this dataset.")

def apply_filters(base_df):
    filtered = base_df.copy()

    st.markdown('<div class="filter-panel"><div class="filter-heading">Filters</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1.15, 1.15, 1.15, 1.65])

    with c1:
        region = st.selectbox("Region", ["All Regions"] + sorted(base_df["region"].dropna().unique().tolist()))

    with c2:
        market = st.selectbox("Market", ["All Markets"] + sorted(base_df["market"].dropna().unique().tolist()))

    with c3:
        category = st.selectbox("Category", ["All Categories"] + sorted(base_df["category"].dropna().unique().tolist()))

    with c4:
        min_year, max_year = int(base_df["year"].min()), int(base_df["year"].max())
        years = st.slider("Years", min_year, max_year, (min_year, max_year))

    st.markdown("</div>", unsafe_allow_html=True)

    if region != "All Regions":
        filtered = filtered[filtered["region"] == region]
    if market != "All Markets":
        filtered = filtered[filtered["market"] == market]
    if category != "All Categories":
        filtered = filtered[filtered["category"] == category]

    filtered = filtered[filtered["year"].between(years[0], years[1])]
    return filtered

# =========================================================
# NAV STATE
# =========================================================
pages = ["Home", "Summary Dashboard", "Detailed Analysis", "Insights & Recommendations"]

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class="top-header">
        <div class="logo-box">🛒</div>
        <div>
            <div class="header-title">Global Superstore Analytics Dashboard</div>
            <div class="header-subtitle">Interactive insights for sales, profit, customers, and operations</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# NAVIGATION
# =========================================================
selected = st.radio(
    "",
    pages,
    index=pages.index(st.session_state.selected_page),
    horizontal=True,
    label_visibility="collapsed"
)
st.session_state.selected_page = selected
page = selected

# =========================================================
# HOME
# =========================================================
if page == "Home":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <h1>Global Superstore Dashboard</h1>
                <p>
                    A professional dashboard designed to monitor sales growth, profitability,
                    customer segments, shipping performance, and market opportunities.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="project-card">
            <h2>About This Project</h2>
            <p>
                This project analyzes the Global Superstore dataset to help decision makers understand
                business performance across regions, markets, products, customers, and shipping operations.
                The dashboard turns raw transactional data into clear KPIs, interactive visuals, and
                actionable recommendations.
            </p>
            <div class="feature-grid">
                <div class="feature-pill">📈 Sales Trends</div>
                <div class="feature-pill">💰 Profitability</div>
                <div class="feature-pill">🌍 Markets</div>
                <div class="feature-pill">👥 Customers</div>
                <div class="feature-pill">🚚 Shipping</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    if st.button("Explore Dashboard →"):
        st.session_state.selected_page = "Summary Dashboard"
        st.rerun()

# =========================================================
# SUMMARY DASHBOARD
# =========================================================
elif page == "Summary Dashboard":
    filtered_df = apply_filters(df)

    st.markdown('<div class="page-shell">', unsafe_allow_html=True)
    section_title("Summary Dashboard", "Executive overview of sales, profit, orders, and return rate.")

    total_sales = filtered_df["sales"].sum()
    total_profit = filtered_df["profit"].sum()
    total_orders = filtered_df["order_id"].nunique()
    return_rate = (filtered_df["returned"] == "Yes").mean() if "returned" in filtered_df.columns and len(filtered_df) else 0

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        kpi_card(f"${total_sales:,.0f}", "Total Sales")
    with c2:
        kpi_card(f"${total_profit:,.0f}", "Total Profit")
    with c3:
        kpi_card(f"{total_orders:,}", "Total Orders")
    with c4:
        kpi_card(f"{return_rate * 100:.1f}%", "Return Rate")

    sales_by_month = filtered_df.groupby("month", as_index=False)["sales"].sum()
    fig1 = px.line(sales_by_month, x="month", y="sales", markers=True, title="Total Sales by Month")
    plot_in_card(fig1)

    sales_by_market = (
        filtered_df.groupby("market", as_index=False)["sales"]
        .sum()
        .sort_values("sales", ascending=False)
        .head(10)
    )
    fig2 = px.bar(sales_by_market, x="market", y="sales", title="Top 10 Markets by Revenue")
    plot_in_card(fig2)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# DETAILED ANALYSIS
# =========================================================
elif page == "Detailed Analysis":
    filtered_df = apply_filters(df)

    st.markdown('<div class="page-shell">', unsafe_allow_html=True)
    section_title("Detailed Analysis", "Explore performance by sales, profit, returns, customers, managers, and shipping.")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Sales", "Profit & Discount", "Returns", "Customers", "Managers", "Shipping"]
    )

    with tab1:
        sales_by_year = filtered_df.groupby("year", as_index=False)["sales"].sum()
        fig = px.line(sales_by_year, x="year", y="sales", markers=True, title="Total Sales by Year")
        fig.update_xaxes(tickmode="linear", dtick=1)
        plot_in_card(fig)

        CHART_HEIGHT = 500
        col1, col2 = st.columns(2)

        with col1:
            sales_by_category = (
                filtered_df.groupby("category", as_index=False)["sales"]
                .sum()
                .sort_values("sales", ascending=False)
            )

            fig = px.bar(
                sales_by_category,
                x="category",
                y="sales",
                title="Sales by Category"
            )
            fig.update_layout(height=CHART_HEIGHT)
            plot_in_card(fig)

        with col2:
            if "product_name" in filtered_df.columns:
                top_products = (
                    filtered_df.groupby("product_name", as_index=False)["sales"]
                    .sum()
                    .sort_values("sales", ascending=False)
                    .head(10)
                )

                fig = px.bar(
                    top_products.sort_values("sales"),
                    x="sales",
                    y="product_name",
                    orientation="h",
                    title="Top 10 Products by Revenue"
                )
                fig.update_layout(
                    yaxis=dict(title="", automargin=True),
                    xaxis=dict(title="Sales"),
                    height=CHART_HEIGHT
                )
                plot_in_card(fig)
            else:
                safe_bar_message("product_name")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            cat_profit = (
                filtered_df.groupby("category", as_index=False)["profit"]
                .sum()
                .sort_values("profit", ascending=False)
            )
            fig = px.bar(cat_profit, x="category", y="profit", title="Profit by Category")
            plot_in_card(fig)

        with col2:
            cat_discount = (
                filtered_df.groupby("category", as_index=False)["discount"]
                .mean()
                .sort_values("discount", ascending=False)
            )
            fig = px.bar(cat_discount, x="category", y="discount", title="Average Discount by Category")
            plot_in_card(fig)

        subcat_col = "sub_category" if "sub_category" in filtered_df.columns else None

        if subcat_col:
            loss_bysubcat = (
                filtered_df[filtered_df["profit"] < 0]
                .groupby(subcat_col, as_index=False)["profit"]
                .sum()
                .sort_values("profit")
            )
            fig = px.bar(loss_bysubcat, x=subcat_col, y="profit", title="Loss-Making Sub-Categories")
            plot_in_card(fig)
        else:
            safe_bar_message("sub_category")

    with tab3:
        if "returned" not in filtered_df.columns:
            st.info("The `returned` column is not available in this dataset.")
        else:
            col1, col2 = st.columns(2)

            with col1:
                return_rate_by_region = (
                    filtered_df.groupby("region")["returned"]
                    .apply(lambda x: (x == "Yes").mean())
                    .reset_index(name="return_rate")
                    .sort_values("return_rate", ascending=False)
                )
                fig = px.bar(return_rate_by_region, x="region", y="return_rate", title="Return Rate by Region")
                plot_in_card(fig)

            with col2:
                return_rate_by_category = (
                    filtered_df.groupby("category")["returned"]
                    .apply(lambda x: (x == "Yes").mean())
                    .reset_index(name="return_rate")
                    .sort_values("return_rate", ascending=False)
                )
                fig = px.bar(return_rate_by_category, x="category", y="return_rate", title="Return Rate by Category")
                plot_in_card(fig)

    with tab4:
        col1, col2 = st.columns(2)

        with col1:
            if "segment" in filtered_df.columns:
                segment_sales = (
                    filtered_df.groupby("segment", as_index=False)["sales"]
                    .sum()
                    .sort_values("sales", ascending=False)
                )
                fig = px.bar(segment_sales, x="segment", y="sales", title="Sales by Customer Segment")
                plot_in_card(fig)
            else:
                safe_bar_message("segment")

        with col2:
            if "person" in filtered_df.columns:
                most_active_person = (
                    filtered_df.groupby(["region", "person"])["order_id"]
                    .count()
                    .reset_index(name="order_count")
                    .sort_values(["region", "order_count"], ascending=[True, False])
                )
                most_active_person = most_active_person.groupby("region").head(1)
                fig = px.bar(most_active_person, x="person", y="order_count", title="Most Active Person by Region")
                plot_in_card(fig)
            else:
                safe_bar_message("person")

        avg_order_value = filtered_df.groupby("order_id")["sales"].sum().mean() if len(filtered_df) else 0
        kpi_card(f"${avg_order_value:,.2f}", "Average Order Value")

    with tab5:
        col1, col2 = st.columns(2)

        if "person" not in filtered_df.columns:
            safe_bar_message("person")
        else:
            with col1:
                sales_by_person = (
                    filtered_df.groupby("person", as_index=False)["sales"]
                    .sum()
                    .sort_values("sales", ascending=False)
                    .head(10)
                )
                fig = px.bar(sales_by_person, x="person", y="sales", title="Sales by Person")
                plot_in_card(fig)

            with col2:
                profit_by_person = (
                    filtered_df.groupby("person", as_index=False)["profit"]
                    .sum()
                    .sort_values("profit", ascending=False)
                    .head(10)
                )
                fig = px.bar(profit_by_person, x="person", y="profit", title="Profit by Person")
                plot_in_card(fig)

    with tab6:
        col1, col2 = st.columns(2)

        with col1:
            if "ship_mode" in filtered_df.columns:
                fig = px.histogram(filtered_df, x="ship_mode", title="Shipping Mode Distribution")
                plot_in_card(fig)
            else:
                safe_bar_message("ship_mode")

        with col2:
            shipping_by_year = (
                filtered_df.groupby(filtered_df["ship_date"].dt.year)["shipping_cost"]
                .sum()
                .reset_index()
            )
            shipping_by_year.columns = ["year", "shipping_cost"]
            fig = px.line(shipping_by_year, x="year", y="shipping_cost", markers=True, title="Total Shipping Cost by Year")
            fig.update_xaxes(tickmode="linear", dtick=1)
            plot_in_card(fig)

        total_shipping_cost = filtered_df["shipping_cost"].sum()
        kpi_card(f"${total_shipping_cost:,.2f}", "Total Shipping Cost")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# INSIGHTS & RECOMMENDATIONS
# =========================================================
elif page == "Insights & Recommendations":
        st.markdown('<div class="page-shell">', unsafe_allow_html=True)
        section_title("Insights & Recommendations", "Actionable findings and recommended business actions.")
    
        # 📊 Data
        insights_data = [
            ["Shipping", "Standard Class is the most used shipping mode", "Optimize Standard shipping costs"],
            ["Customer Segment", "Consumer segment drives most revenue", "Focus marketing on Consumer segment"],
            ["Category Demand", "Office Supplies has consistent demand", "Maintain strong stock levels"],
            ["Sub-Category", "Binders are highly ordered", "Bundle with related products"],
            ["Market", "Asia Pacific performs strongly", "Expand in Asia Pacific"],
            ["Sales Pattern", "Sales are right-skewed", "Increase mid-value orders"],
            ["Profit", "High variability in profit margins", "Standardize pricing strategies"],
            ["Top Category", "Technology is most profitable", "Promote Technology products"],
            ["Discount Risk", "Furniture has high discounts", "Reduce excessive discounting"],
            ["Loss Areas", "Tables generate losses", "Adjust pricing or reduce cost"],
            ["Returns", "Eastern Africa has high returns", "Improve logistics & quality"],
            ["Category Returns", "Office Supplies returns are high", "Improve product quality"],
        ]
    
        df_insights = pd.DataFrame(
            insights_data,
            columns=["Area", "Insight", "Recommendation"]
        )
    
        
        st.markdown(
            df_insights.to_html(index=False, classes="insights-table"),
            unsafe_allow_html=True
    <hr>
        )
    
        st.markdown("</div>", unsafe_allow_html=True)
# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">Built with Streamlit • Global Superstore Project</div>
""", unsafe_allow_html=True)
