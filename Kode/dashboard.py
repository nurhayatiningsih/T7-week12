# Nama  : Nurhayati Ningsih
# NIM   : F1D02410085
# Kelas : C

import pandas as pd
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
    QLabel, QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QSplitter, QFrame, QMessageBox, QFileDialog,
    QAbstractItemView,
)
from PySide6.QtCore import Qt
from dataset import load_data, get_filter_options
from plots import MplCanvas, CHART_FUNCS

class SummaryCard(QFrame):
    def __init__(self, title, color="#2E86AB"):
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet(f"SummaryCard {{ background: white; border: 1px solid #E0E0E0; border-radius: 8px; border-left: 4px solid {color}; }}")
        self.setFixedHeight(80)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(12, 8, 12, 8)
        self.lbl_title = QLabel(title)
        self.lbl_title.setStyleSheet("color:#888; font-size:11px;")
        lay.addWidget(self.lbl_title)
        self.lbl_val = QLabel("0")
        self.lbl_val.setStyleSheet(f"color:{color}; font-size:20px; font-weight:bold;")
        lay.addWidget(self.lbl_val)
        lay.addStretch()

    def set_val(self, v):
        self.lbl_val.setText(f"{v:,.2f}" if isinstance(v, float) else f"{v:,}")

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Visualisasi Data — Supermarket Sales")
        self.setMinimumSize(1280, 820)
        self.resize(1400, 880)
        self.df_all = load_data()
        self.df = self.df_all.copy()
        self.combos = {}
        self._build()
        self._fill_filters()
        self._refresh_all()

    def _build(self):
        cw = QWidget()
        self.setCentralWidget(cw)
        root = QVBoxLayout(cw)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(8)

        hdr = QFrame()
        hdr.setStyleSheet("background:qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 #2E86AB,stop:1 #1B6B93); border-radius:10px;")
        hl = QHBoxLayout(hdr)
        hl.setContentsMargins(18, 10, 18, 10)
        t = QLabel("Dashboard Visualisasi Data — Supermarket Sales")
        t.setStyleSheet("color:white; font-size:17px; font-weight:bold;")
        hl.addWidget(t)
        hl.addStretch()
        s = QLabel("PySide6 • Matplotlib • Pandas")
        s.setStyleSheet("color:rgba(255,255,255,0.7); font-size:11px;")
        hl.addWidget(s)
        root.addWidget(hdr)

        sw = QWidget()
        sl = QHBoxLayout(sw)
        sl.setContentsMargins(0,0,0,0); sl.setSpacing(8)
        self.c_rev = SummaryCard("Total Pendapatan", "#2E86AB")
        self.c_cnt = SummaryCard("Jumlah Transaksi", "#A23B72")
        self.c_avg = SummaryCard("Rata-rata Transaksi", "#F18F01")
        self.c_qty = SummaryCard("Total Item Terjual", "#44BBA4")
        self.c_rat = SummaryCard("Rata-rata Rating", "#E94F37")
        for c in [self.c_rev, self.c_cnt, self.c_avg, self.c_qty, self.c_rat]: sl.addWidget(c)
        root.addWidget(sw)

        fg = QGroupBox("Filter & Kontrol")
        fg.setStyleSheet("QGroupBox { font-weight:bold; font-size:12px; border:1px solid #E0E0E0; border-radius:8px; margin-top:10px; padding-top:14px; } QGroupBox::title { subcontrol-origin:margin; left:12px; padding:0 5px; color:#333; }")
        fl = QVBoxLayout(fg); fl.setContentsMargins(12, 6, 12, 6)

        r1 = QHBoxLayout(); r1.setSpacing(8)
        nama_filter = {"branch": "Cabang", "city": "Kota", "customer_type": "Tipe Pelanggan", "product_line": "Kategori Produk", "payment": "Pembayaran"}
        for col, label in nama_filter.items():
            r1.addWidget(QLabel(label + ":"))
            cb = QComboBox(); cb.setMinimumWidth(120)
            cb.setStyleSheet("color: black; background-color: white; border: 1px solid #ccc; padding: 5px;")
            cb.currentTextChanged.connect(self._on_filter)
            self.combos[col] = cb; r1.addWidget(cb)
        r1.addStretch(); fl.addLayout(r1)

        r2 = QHBoxLayout(); r2.setSpacing(8)
        r2.addWidget(QLabel("Tipe Chart:"))
        self.cb_chart = QComboBox(); self.cb_chart.setMinimumWidth(300)
        self.cb_chart.setStyleSheet("color: black; background-color: white; border: 1px solid #ccc; padding: 5px;")
        self.cb_chart.addItems(CHART_FUNCS.keys())
        self.cb_chart.currentTextChanged.connect(self._draw_chart)
        r2.addWidget(self.cb_chart); r2.addStretch()

        btn_style = "QPushButton{{background:{bg};color:white;border:none;border-radius:5px;padding:7px 14px;font-weight:bold;font-size:11px;}}QPushButton:hover{{background:{hv};}}"
        b_ref = QPushButton("Refresh Data"); b_ref.setStyleSheet(btn_style.format(bg="#2E86AB", hv="#1B6B93")); b_ref.clicked.connect(self._do_refresh); r2.addWidget(b_ref)
        b_exp = QPushButton("Export Chart ke PNG"); b_exp.setStyleSheet(btn_style.format(bg="#44BBA4", hv="#2E9E8F")); b_exp.clicked.connect(self._do_export); r2.addWidget(b_exp)
        b_rst = QPushButton("Reset Filter"); b_rst.setStyleSheet(btn_style.format(bg="#E94F37", hv="#C73E1D")); b_rst.clicked.connect(self._do_reset); r2.addWidget(b_rst)
        fl.addLayout(r2); root.addWidget(fg)

        sp = QSplitter(Qt.Vertical); sp.setStyleSheet("QSplitter::handle{background:#E0E0E0;height:3px;}")
        cg = QGroupBox("Visualisasi Chart"); cg.setStyleSheet("QGroupBox{font-weight:bold;font-size:12px;border:1px solid #E0E0E0;border-radius:8px;margin-top:10px;padding-top:14px;}QGroupBox::title{subcontrol-origin:margin;left:12px;padding:0 5px;color:#333;}")
        cl = QVBoxLayout(cg); cl.setContentsMargins(8, 4, 8, 8); self.canvas = MplCanvas(self); cl.addWidget(self.canvas); sp.addWidget(cg)

        tg = QGroupBox("Data Tabel"); tg.setStyleSheet("QGroupBox{font-weight:bold;font-size:12px;border:1px solid #E0E0E0;border-radius:8px;margin-top:10px;padding-top:14px;}QGroupBox::title{subcontrol-origin:margin;left:12px;padding:0 5px;color:#333;}")
        tl = QVBoxLayout(tg); tl.setContentsMargins(8, 4, 8, 8)
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True); self.table.setEditTriggers(QAbstractItemView.NoEditTriggers); self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.verticalHeader().setVisible(False); self.table.verticalHeader().setDefaultSectionSize(24); self.table.setMinimumHeight(160)
        self.table.setStyleSheet("QTableWidget { gridline-color:#E0E0E0; font-size:11px; color: black; background-color: white; selection-background-color:#2E86AB; selection-color:white; alternate-background-color:#F5F7FA; } QHeaderView::section { background:#2E86AB; color:white; padding:4px; border:1px solid #1B6B93; font-weight:bold; font-size:10px; }")
        tl.addWidget(self.table); sp.addWidget(tg)
        sp.setStretchFactor(0, 6); sp.setStretchFactor(1, 4); sp.setSizes([500, 320]); root.addWidget(sp, 1)
        self.statusBar().setStyleSheet("color:#666;padding:3px;"); self.statusBar().showMessage("Siap")

    def closeEvent(self, event):
        msg = QMessageBox.question(self, "Keluar", "Yakin mau tutup aplikasi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes: event.accept()
        else: event.ignore()

    def _fill_filters(self):
        opts = get_filter_options(self.df_all)
        for col, vals in opts.items():
            if col in self.combos:
                self.combos[col].blockSignals(True); self.combos[col].clear(); self.combos[col].addItems(vals); self.combos[col].blockSignals(False)

    def _on_filter(self):
        df = self.df_all.copy()
        for col, cb in self.combos.items():
            v = cb.currentText()
            if v != "Semua" and col in df.columns: df = df[df[col] == v]
        self.df = df; self._refresh_all()

    def _do_reset(self):
        msg = QMessageBox.question(self, "Reset Filter", "Reset semua filter ke awal?", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            for cb in self.combos.values(): cb.blockSignals(True); cb.setCurrentIndex(0); cb.blockSignals(False)
            self._on_filter()

    def _do_refresh(self):
        msg = QMessageBox.question(self, "Refresh Data", "Muat ulang data dari file CSV?", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.df_all = load_data(); self._fill_filters()
            for cb in self.combos.values(): cb.blockSignals(True); cb.setCurrentIndex(0); cb.blockSignals(False)
            self._on_filter(); self.statusBar().showMessage("Data berhasil di-refresh!", 3000)

    def _refresh_all(self):
        self._update_cards(); self._update_table(); self._draw_chart(); self._update_status()

    def _update_cards(self):
        d = self.df
        self.c_rev.set_val(d["total"].sum() if not d.empty else 0)
        self.c_cnt.set_val(len(d))
        self.c_avg.set_val(d["total"].mean() if not d.empty else 0)
        self.c_qty.set_val(d["quantity"].sum() if not d.empty else 0)
        self.c_rat.set_val(round(d["rating"].mean(), 1) if not d.empty else 0)

    def _update_table(self):
        d = self.df
        cols = ["invoice_id", "branch", "city", "customer_type", "gender", "product_line", "unit_price", "quantity", "total", "date", "payment", "rating"]
        cols = [c for c in cols if c in d.columns]
        nama = {"invoice_id": "Invoice ID", "branch": "Cabang", "city": "Kota", "customer_type": "Tipe Pelanggan", "gender": "Gender", "product_line": "Kategori Produk", "unit_price": "Harga Satuan", "quantity": "Qty", "total": "Total", "date": "Tanggal", "payment": "Pembayaran", "rating": "Rating"}
        money = {"unit_price", "total", "tax_5%", "cogs", "gross_income"}
        self.table.setRowCount(len(d)); self.table.setColumnCount(len(cols))
        self.table.setHorizontalHeaderLabels([nama.get(c, c) for c in cols])
        for r, (_, row) in enumerate(d.iterrows()):
            for c, col in enumerate(cols):
                val = row[col]
                if col == "date": txt = val.strftime("%Y-%m-%d") if hasattr(val, "strftime") else str(val)
                elif col in money: txt = f"${val:,.2f}" if pd.notna(val) else "N/A"
                elif col == "rating": txt = f"{val:.1f}" if pd.notna(val) else "N/A"
                else: txt = str(val) if pd.notna(val) else "N/A"
                item = QTableWidgetItem(txt); item.setTextAlignment(Qt.AlignCenter); self.table.setItem(r, c, item)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def _draw_chart(self):
        name = self.cb_chart.currentText()
        if name in CHART_FUNCS: CHART_FUNCS[name](self.canvas, self.df)

    def _do_export(self):
        msg = QMessageBox.question(self, "Export PNG", "Simpan chart sekarang?", QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.No: return
        safe = self.canvas.get_title().replace(" ", "_").replace("—", "").strip()
        if not safe: safe = "chart"
        path, _ = QFileDialog.getSaveFileName(self, "Simpan Chart", f"{safe}.png", "PNG (*.png)")
        if path:
            try:
                self.canvas.export_png(path); self.statusBar().showMessage(f"Disimpan: {path}", 4000)
                QMessageBox.information(self, "Berhasil", f"Chart tersimpan di:\n{path}")
            except Exception as e: QMessageBox.critical(self, "Error", f"Gagal save:\n{str(e)}")

    def _update_status(self):
        aktif = []
        nm = {"branch": "Cabang", "city": "Kota", "customer_type": "Pelanggan", "product_line": "Produk", "payment": "Pembayaran"}
        for col, cb in self.combos.items():
            v = cb.currentText()
            if v != "Semua": aktif.append(f"{nm[col]}: {v}")
        f = " | ".join(aktif) if aktif else "Tidak ada filter"
        self.statusBar().showMessage(f"{len(self.df)} dari {len(self.df_all)} record | {f}")