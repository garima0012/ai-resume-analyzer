"""
visualizer.py – Plotly chart helpers for the Streamlit dashboard.
"""
from __future__ import annotations
import plotly.graph_objects as go


ACCENT = "#00f5a0"
ACCENT2 = "#00d9f5"
WARN = "#ffb347"
DANGER = "#ff4b4b"
BG = "rgba(0,0,0,0)"
PAPER = "rgba(0,0,0,0)"
FONT_COLOR = "#cccccc"
GRID_COLOR = "rgba(255,255,255,0.06)"


def _base_layout(**kwargs) -> dict:
    return dict(
        paper_bgcolor=PAPER,
        plot_bgcolor=BG,
        font=dict(color=FONT_COLOR, family="DM Sans, sans-serif"),
        margin=dict(t=20, b=20, l=10, r=10),
        **kwargs,
    )


def render_score_gauge(score: int) -> go.Figure:
    color = ACCENT if score >= 70 else WARN if score >= 40 else DANGER
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "%", "font": {"size": 40, "color": color}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": FONT_COLOR},
                "bar": {"color": color},
                "bgcolor": "rgba(255,255,255,0.05)",
                "steps": [
                    {"range": [0, 40], "color": "rgba(255,75,75,0.1)"},
                    {"range": [40, 70], "color": "rgba(255,179,71,0.1)"},
                    {"range": [70, 100], "color": "rgba(0,245,160,0.1)"},
                ],
                "threshold": {"line": {"color": color, "width": 3}, "value": score},
            },
        )
    )
    fig.update_layout(**_base_layout(height=220))
    return fig


def render_skill_match_chart(matched: int, missing: int) -> go.Figure:
    fig = go.Figure(
        go.Pie(
            labels=["Matched Skills", "Missing Skills"],
            values=[max(matched, 0), max(missing, 0)],
            hole=0.65,
            marker=dict(colors=[ACCENT, DANGER],
                        line=dict(color="#0d0d0d", width=3)),
            textfont=dict(size=12, color=FONT_COLOR),
            hovertemplate="%{label}: %{value}<extra></extra>",
        )
    )
    fig.update_layout(**_base_layout(height=260, showlegend=True,
                                     legend=dict(orientation="h", yanchor="bottom",
                                                 y=-0.2, xanchor="center", x=0.5)))
    return fig


def render_section_scores(section_scores: dict[str, int]) -> go.Figure:
    categories = list(section_scores.keys())
    values = list(section_scores.values())

    colors = [
        ACCENT if v >= 70 else WARN if v >= 40 else DANGER
        for v in values
    ]

    fig = go.Figure(
        go.Bar(
            x=values,
            y=categories,
            orientation="h",
            marker=dict(color=colors, line=dict(width=0)),
            text=[f"{v}%" for v in values],
            textposition="outside",
            textfont=dict(color=FONT_COLOR, size=12),
            hovertemplate="%{y}: %{x}%<extra></extra>",
        )
    )
    fig.update_layout(
        **_base_layout(height=260),
        xaxis=dict(range=[0, 115], showgrid=True, gridcolor=GRID_COLOR,
                   ticksuffix="%", tickfont=dict(color=FONT_COLOR)),
        yaxis=dict(showgrid=False, tickfont=dict(color=FONT_COLOR, size=13)),
        bargap=0.35,
    )
    return fig
