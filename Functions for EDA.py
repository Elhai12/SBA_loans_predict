import pandas as pd
import plotly.express as px

def percent_paid_not_paid(df_for_eda,col_groups):
#Function for create df contains the percent of paid and not paid for each group in column
    df_all = df_for_eda[col_groups].value_counts()
    df_paid = df_for_eda[df_for_eda['MIS_Status'] == 0][col_groups].value_counts()
    df_unpaid = df_for_eda[df_for_eda['MIS_Status'] == 1][col_groups].value_counts()
    df_concat = pd.concat([df_all, df_paid, df_unpaid], axis=1)
    df_concat.columns = ['all', 'paid', 'unpaid']
    df_concat['paid_perc'] = df_concat['paid'] / df_concat['all']
    df_concat['unpaid_perc'] = df_concat['unpaid'] / df_concat['all']
    df_concat = df_concat.sort_index(ascending=False)
    return df_concat

def plotly_lines(df_concat):
#Function to create compare lines of paid and not paid percentage
    fig = px.line(
        df_concat,
        x=df_concat.index,
        y=['unpaid_perc', 'paid_perc'],
        labels={'value': 'Percentage', 'variable': 'Metric'},
        title='Unpaid Percentage and Paid Percentage Over Time'
    )

    fig.update_layout(
        xaxis_title="Approve year loan",
        yaxis_title="Percentage (%)",
        legend_title="Paid/Unpaid"
    )
    return fig