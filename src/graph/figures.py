import plotly.express as px

"""
Wonder why we call this for the GraphBuilder instead of
get(attr, figure)? It doesn't work
"""


figures = {
    "scatter":px.scatter,
    "scatter_3d":px.scatter_3d,
    "scatter_polar":px.scatter_polar,
    "scatter_ternary":px.scatter_ternary,
    "scatter_mapbox":px.scatter_mapbox,
    "scatter_geo":px.scatter_geo,
    "line":px.line,
    "line_3d":px.line_3d,
    "line_polar":px.line_polar,
    "line_ternary":px.line_ternary,
    "line_mapbox":px.line_mapbox,
    "line_geo":px.line_geo,
    "area":px.area,
    "bar":px.bar,
    "timeline":px.timeline,
    "bar_polar":px.bar_polar,
    "violin":px.violin,
    "box":px.box,
    "strip":px.strip,
    "histogram":px.histogram,
    "ecdf":px.ecdf,
    "scatter_matrix":px.scatter_matrix,
    "parallel_coordinates":px.parallel_coordinates,
    "parallel_categories":px.parallel_categories,
    "choropleth":px.choropleth,
    "density_contour":px.density_contour,
    "density_heatmap":px.density_heatmap,
    "pie":px.pie,
    "sunburst":px.sunburst,
    "treemap":px.treemap,
    "icicle":px.icicle,
    "funnel":px.funnel,
    "funnel_area":px.funnel_area,
    "choropleth_mapbox":px.choropleth_mapbox,
    "density_mapbox":px.density_mapbox,
}
