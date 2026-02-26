import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np


def create_visuals(df, output_dir="data/visualisations"):
    os.makedirs(output_dir, exist_ok=True)
    sns.set(style="whitegrid")

    # total sales per product category
    category_sales = df.groupby("product_category")["total"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category_sales.index, y=category_sales.values, ax=ax, palette="pastel")
    ax.set_title("Total Sales by Product Category")
    ax.set_ylabel("Total Sales")
    plt.tight_layout()
    ax_fig_path = os.path.join(output_dir, "sales_by_category.png")
    plt.savefig(ax_fig_path, dpi=150)
    plt.savefig(ax_svg_path)
    plt.close()

    # quantity vs price scatter plot with marker size based on total sales
    df_plot = df.copy()
    # create a marker size based on total 
    if "total" in df_plot.columns and df_plot["total"].notnull().any():
        tmin = df_plot["total"].min()
        tmax = df_plot["total"].max()
        if tmax > tmin:
            df_plot["marker_size"] = ((df_plot["total"] - tmin) / (tmax - tmin)) * 220 + 30
        else:
            df_plot["marker_size"] = 80
    else:
        df_plot["marker_size"] = 60

    plt.figure(figsize=(10, 6))
    ax2 = sns.scatterplot(
        data=df_plot,
        x="quantity",
        y="price",
        hue="product_category",
        size="marker_size",
        sizes=(30, 300),
        palette="tab10",
        alpha=0.75,
        edgecolor="w",
        linewidth=0.5,
    )

    # add a global trend line
    try:
        sns.regplot(data=df_plot, x="quantity", y="price", scatter=False, ax=ax2, color="k", line_kws={"linewidth": 1, "alpha": 0.6})
    except Exception:
        pass

    ax2.set_title("Quantity vs Price (marker size ~ total sales)")
    ax2.set_xlabel("Quantity")
    ax2.set_ylabel("Price")
    # move legend outside
    handles, labels = ax2.get_legend_handles_labels()
    if handles:
        ax2.legend(handles=handles, labels=labels, bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0)

    plt.tight_layout()
    scatter_png = os.path.join(output_dir, "quantity_vs_price.png")
    plt.savefig(scatter_png, dpi=150, bbox_inches="tight")
    plt.savefig(scatter_svg, bbox_inches="tight")
    plt.close()

    print(f"Visualizations saved to {output_dir}")