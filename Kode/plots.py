# Nama  : Nurhayati Ningsih
# NIM   : F1D02410085
# Kelas : C

import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QSizePolicy

COLORS = ["#2E86AB", "#A23B72", "#F18F01", "#C73E1D", "#44BBA4", "#E94F37"]

try:
    plt.style.use("seaborn-v0_8-whitegrid")
except:
    try:
        plt.style.use("seaborn-whitegrid")
    except:
        pass

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=4.5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#FAFAFA")
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def export_png(self, filepath):
        self.fig.savefig(filepath, dpi=150, bbox_inches="tight", facecolor="white")

    def get_title(self):
        t = self.axes.get_title()
        return t if t else "chart"

def _no_data(canvas):
    canvas.fig.clear()
    ax = canvas.fig.add_subplot(111)
    canvas.axes = ax
    ax.text(0.5, 0.5, "Tidak ada data", ha="center", va="center", fontsize=16, color="gray", transform=ax.transAxes)
    canvas.fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
    canvas.draw()

def draw_bar_produk(canvas, df):
    if df.empty: _no_data(canvas); return
    canvas.fig.clear()
    ax = canvas.fig.add_subplot(111)
    canvas.axes = ax
    
    s = df.groupby("product_line")["total"].sum().sort_values(ascending=True)
    ax.barh(s.index, s.values, color=COLORS[:len(s)], height=0.6)
    mx = s.max()
    for i, (v, name) in enumerate(zip(s.values, s.index)):
        ax.text(v + mx * 0.01, i, f"${v:,.2f}", va="center", fontsize=9)
    ax.set_xlabel("Total Penjualan ($)", fontweight="bold")
    ax.set_title("Penjualan per Kategori Produk", fontweight="bold", pad=15)
    canvas.fig.subplots_adjust(left=0.25, right=0.85, top=0.9, bottom=0.15)
    canvas.draw()

def draw_pie_cabang(canvas, df):
    if df.empty: _no_data(canvas); return
    canvas.fig.clear()
    ax = canvas.fig.add_subplot(111)
    canvas.axes = ax
    
    s = df.groupby("branch")["total"].sum()
    city = df.groupby("branch")["city"].first()
    labels = [f"Cabang {b} ({city[b]})" for b in s.index]
    ax.pie(s.values, labels=labels, autopct="%1.1f%%", colors=COLORS[:len(s)], startangle=90, explode=[0.03]*len(s), shadow=True)
    ax.set_title("Distribusi Penjualan per Cabang", fontweight="bold", pad=15)
    canvas.fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    canvas.draw()

def draw_line_harian(canvas, df):
    if df.empty: _no_data(canvas); return
    canvas.fig.clear()
    ax = canvas.fig.add_subplot(111)
    canvas.axes = ax
    
    d = df.groupby("date")["total"].sum().sort_index()
    ax.plot(d.index, d.values, color="#2E86AB", linewidth=2, marker="o", markersize=4)
    ax.fill_between(d.index, d.values, alpha=0.1, color="#2E86AB")
    ax.set_xlabel("Tanggal", fontweight="bold")
    ax.set_ylabel("Total ($)", fontweight="bold")
    ax.set_title("Tren Penjualan Harian", fontweight="bold", pad=15)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
    canvas.fig.subplots_adjust(left=0.12, right=0.9, top=0.9, bottom=0.22)
    canvas.draw()

def draw_grouped_cabang(canvas, df):
    if df.empty: _no_data(canvas); return
    canvas.fig.clear()
    ax = canvas.fig.add_subplot(111)
    canvas.axes = ax
    
    pv = df.groupby(["branch", "customer_type"])["total"].sum().unstack(fill_value=0)
    if pv.empty: _no_data(canvas); return
    
    city = df.groupby("branch")["city"].first()
    x = range(len(pv.index)); w = 0.3
    for i, col in enumerate(pv.columns):
        off = (i - (len(pv.columns)-1)/2) * w
        ax.bar([xi + off for xi in x], pv[col], w, label=col, color=COLORS[i])
        
    ax.set_xticks(list(x))
    ax.set_xticklabels([f"Cabang {b}\n({city[b]})" for b in pv.index])
    ax.set_ylabel("Total ($)", fontweight="bold")
    ax.set_title("Penjualan per Cabang & Tipe Pelanggan", fontweight="bold", pad=15)
    ax.legend()
    canvas.fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
    canvas.draw()

def draw_bar_payment(canvas, df):
    if df.empty: _no_data(canvas); return
    canvas.fig.clear()
    ax = canvas.fig.add_subplot(111)
    canvas.axes = ax
    
    s = df.groupby("payment")["total"].sum().sort_values(ascending=False)
    ax.bar(s.index, s.values, color=COLORS[:len(s)], width=0.5)
    mx = s.max()
    for i, (name, v) in enumerate(s.items()):
        ax.text(i, v + mx*0.01, f"${v:,.2f}", ha="center", fontsize=9, fontweight="bold")
    ax.set_ylabel("Total ($)", fontweight="bold")
    ax.set_title("Penjualan per Metode Pembayaran", fontweight="bold", pad=15)
    canvas.fig.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
    canvas.draw()

CHART_FUNCS = {
    "Bar Chart — Penjualan per Produk": draw_bar_produk,
    "Pie Chart — Distribusi per Cabang": draw_pie_cabang,
    "Line Chart — Tren Harian": draw_line_harian,
    "Grouped Bar — Cabang & Tipe Pelanggan": draw_grouped_cabang,
    "Bar Chart — Metode Pembayaran": draw_bar_payment,
}