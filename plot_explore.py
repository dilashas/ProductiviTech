import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

def createPlots(pctg1, pctg2):

    labels = ["Attentive", "Lost Focus"]

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])

    fig2 = make_subplots(rows=1, cols=1, specs=[[{'barmode':'stack'}]])

    s1colors = ['rgb(251, 121, 91)', 'rgb(253, 214, 206)']

    # s2colors = ['rgb(69, 83, 97)', 'rgb(180, 191, 202)']


    fig.add_trace(go.Pie(labels=labels, values=[pctg1,pctg2], name="Student 1", marker_colors= s1colors),
                  1, 1)
    # fig.add_trace(go.Pie(labels=labels, values=[75,25], name="Student 2", marker_colors = s2colors),
    #               1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.6, hoverinfo="label+percent+name")

    fig.update_layout(
        # title_text="Global Emissions 1990-2011",
        # Add annotations in the center of the donut pies.
        # annotations=[dict(text='80%', x=0.2, y=0.5, font_size=26, showarrow=False),
        #              dict(text='75%', x=0.80, y=0.5, font_size=26, showarrow=False)]

        showlegend=False,
        margin=go.layout.Margin(
            l=0,  # left margin
            r=0,  # right margin
            b=0,  # bottom margin
            t=0  # top margin
        )
    )
    # fig.show()

    #
    username = 'TeodorDev'
    # your username
    api_key = 'mK5siQqDPpxhBelrYy2t'
    # # your api key - go to profile > settings > regenerate key

    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    #
    urlPlotly = py.plot(fig, filename='TestTeo', auto_open=True)
    # #
    print(urlPlotly)
    #
    # # pio.write_html(fig, file='/Users/dilashashrestha/Desktop/index3.html', auto_open=True)
    #
    #
    #
    iFrame = tls.get_embed(urlPlotly)
    #
    print(iFrame)
#change to your url

# createPlots(80,20)

# s2colors = ['rgb(69, 83, 97)', 'rgb(180, 191, 202)']

colors = ['rgb(69, 83, 97)', 'rgb(251, 121, 91)']

fig = go.Figure(data=[go.Bar(
    x=['Present', 'Expected'],
    y=[4, 6],
    marker_color=colors, # marker color can be a single color value or an iterable
    width=[0.6,0.6]
)])
fig.update_layout(
    bargap=0.10,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode='group',
    xaxis_tickangle=-30,
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
    )


fig.update_layout(

)
# fig.show()

username = 'TeodorDev'
# your username
api_key = 'mK5siQqDPpxhBelrYy2t'
# # your api key - go to profile > settings > regenerate key

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
#
urlPlotly = py.plot(fig, filename='TestTeo2', auto_open=True)
# #
print(urlPlotly)
#
# # pio.write_html(fig, file='/Users/dilashashrestha/Desktop/index3.html', auto_open=True)
#
#
#
iFrame = tls.get_embed(urlPlotly)
#
print(iFrame)