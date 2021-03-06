from bokeh.io import save
from bokeh.models import Label, LinearAxis, Plot, Range1d

# Have to specify x/y range as labels aren't included in the plot area solver
plot = Plot(plot_width=600, plot_height=600,
            x_range=Range1d(0, 10), y_range=Range1d(0, 10),
            toolbar_location=None)

label1 = Label(x=1, y=6, x_offset=25, y_offset=25,
               text="Demo Label",
               text_font_size='50px', text_color='red', text_alpha=0.9,
               text_baseline='bottom', text_align='left',
               background_fill_color='green', background_fill_alpha=0.2,
               angle=15, angle_units='deg',
               render_mode='canvas')

label2 = Label(x=3, y=5.5, text="(I'm Canvas)", text_font_size='26px',
               border_line_color='black', border_line_width=2, border_line_dash='8 4',
               render_mode='canvas')

label3 = Label(x=1, y=2, x_offset=25, y_offset=25,
               text="Demo Label",
               text_font_size='50px', text_color='red', text_alpha=0.9,
               text_baseline='bottom', text_align='left',
               background_fill_color='green', background_fill_alpha=0.2,
               angle=0.261, angle_units='rad',
               render_mode='css')

label4 = Label(x=3, y=1.0, text="(I'm CSS)", text_font_size='26px',
               border_line_color='black', border_line_width=2, border_line_dash='8 4',
               render_mode='css')

label_above = Label(
    x=0, y=0, text="Label in above panel", x_units='screen', y_units='screen',
    text_font_size='50px', text_color='firebrick', text_alpha=0.9,
)

label_left = Label(
    x=0, y=0, text="Label in left panel",
    x_units='screen', y_units='screen', angle=90, angle_units='deg',
    text_font_size='24px', text_color='firebrick', text_alpha=0.9,
    background_fill_color='aliceblue', text_baseline='top',
)

plot.add_layout(LinearAxis(), 'below')
plot.add_layout(LinearAxis(), 'left')

plot.add_layout(label1)
plot.add_layout(label2)
plot.add_layout(label3)
plot.add_layout(label4)
plot.add_layout(label_above, 'above')
plot.add_layout(label_left, 'left')

save(plot)
