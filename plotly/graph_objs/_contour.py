from plotly.basedatatypes import BaseTraceType
import copy


class Contour(BaseTraceType):

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `colorscale`. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default  palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autocolorscale']

    @autocolorscale.setter
    def autocolorscale(self, val):
        self['autocolorscale'] = val

    # autocontour
    # -----------
    @property
    def autocontour(self):
        """
        Determines whether or not the contour level attributes are
        picked by an algorithm. If *true*, the number of contour levels
        can be set in `ncontours`. If *false*, set the contour level
        attributes in `contours`.
    
        The 'autocontour' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autocontour']

    @autocontour.setter
    def autocontour(self, val):
        self['autocontour'] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of plotly.graph_objs.contour.ColorBar
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to *log* and *date*
                    axes. If the axis `type` is *log*, then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. *log*
                    has several special values; *L<f>*, where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = *L0.5* will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use *D1* (all
                    digits) or *D2* (only 2 and 5). `tick0` is
                    ignored for *D1* and *D2*. If the axis `type`
                    is *date*, then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. *date* also has special values
                    *M<n>* gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to *2000-01-15* and `dtick` to *M3*. To
                    set ticks every 4 years, set `dtick` to *M48*
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If *none*, it appears as
                    1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
                    *power*, 1x10^9 (with 9 in a super script). If
                    *SI*, 1G. If *B*, 1B.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot *fraction*
                    or in *pixels. Use `len` to set the value.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to *auto*.
                outlinecolor
                    Sets the axis line color.
                outlinewidth
                    Sets the width (in px) of the axis line.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If *all*, all exponents are shown besides their
                    significands. If *first*, only the exponent of
                    the first tick is shown. If *last*, only the
                    exponent of the last tick is shown. If *none*,
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If *all*, all tick labels are displayed with a
                    prefix. If *first*, only the first tick is
                    displayed with a prefix. If *last*, only the
                    last tick is displayed with a suffix. If
                    *none*, tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot *fraction*
                    or in *pixels*. Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    *log*, then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is *date*, it should be a date
                    string, like date data. If the axis `type` is
                    *category*, it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: *%{n}f*
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat *%H~%M~%S.%2f* would display
                    *09~15~23.46*
                tickformatstops
                    plotly.graph_objs.contour.colorbar.Tickformatst
                    op instance or dict with compatible properties
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If *auto*,
                    the number of ticks is set via `nticks`. If
                    *linear*, the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` (*linear* is the default
                    value if `tick0` and `dtick` are provided). If
                    *array*, the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    (*array* is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    **, this axis' ticks are not drawn. If
                    *outside* (*inside*), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to *array*. Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to *array*. Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on plot.ly for
                    tickvals .
                tickwidth
                    Sets the tick width (in px).
                title
                    Sets the title of the color bar.
                titlefont
                    Sets this color bar's title font.
                titleside
                    Determines the location of the colorbar title
                    with respect to the color bar.
                x
                    Sets the x position of the color bar (in plot
                    fraction).
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the *left*, *center* or *right* of the color
                    bar.
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                y
                    Sets the y position of the color bar (in plot
                    fraction).
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    *top*, *middle* or *bottom* of the color bar.
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.

        Returns
        -------
        plotly.graph_objs.contour.ColorBar
        """
        return self['colorbar']

    @colorbar.setter
    def colorbar(self, val):
        self['colorbar'] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use`zmin` and `zmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Bl
        ues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth,Electric,Vi
        ridis,Cividis.
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis']

        Returns
        -------
        str
        """
        return self['colorscale']

    @colorscale.setter
    def colorscale(self, val):
        self['colorscale'] = val

    # connectgaps
    # -----------
    @property
    def connectgaps(self):
        """
        Determines whether or not gaps (i.e. {nan} or missing values)
        in the `z` data are filled in.
    
        The 'connectgaps' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['connectgaps']

    @connectgaps.setter
    def connectgaps(self, val):
        self['connectgaps'] = val

    # contours
    # --------
    @property
    def contours(self):
        """
        The 'contours' property is an instance of Contours
        that may be specified as:
          - An instance of plotly.graph_objs.contour.Contours
          - A dict of string/value properties that will be passed
            to the Contours constructor
    
            Supported dict properties:
                
                coloring
                    Determines the coloring method showing the
                    contour values. If *fill*, coloring is done
                    evenly between each contour level If *heatmap*,
                    a heatmap gradient coloring is applied between
                    each contour level. If *lines*, coloring is
                    done on the contour lines. If *none*, no
                    coloring is applied on this trace.
                end
                    Sets the end contour level value. Must be more
                    than `contours.start`
                labelfont
                    Sets the font used for labeling the contour
                    levels. The default color comes from the lines,
                    if shown. The default family and size come from
                    `layout.font`.
                labelformat
                    Sets the contour label formatting rule using d3
                    formatting mini-language which is very similar
                    to Python, see: https://github.com/d3/d3-format
                    /blob/master/README.md#locale_format.
                operation
                    Sets the constraint operation. *=* keeps
                    regions equal to `value` *<* and *<=* keep
                    regions less than `value` *>* and *>=* keep
                    regions greater than `value` *[]*, *()*, *[)*,
                    and *(]* keep regions inside `value[0]` to
                    `value[1]` *][*, *)(*, *](*, *)[* keep regions
                    outside `value[0]` to value[1]` Open vs. closed
                    intervals make no difference to constraint
                    display, but all versions are allowed for
                    consistency with filter transforms.
                showlabels
                    Determines whether to label the contour lines
                    with their values.
                showlines
                    Determines whether or not the contour lines are
                    drawn. Has an effect only if
                    `contours.coloring` is set to *fill*.
                size
                    Sets the step between each contour level. Must
                    be positive.
                start
                    Sets the starting contour level value. Must be
                    less than `contours.end`
                type
                    If `levels`, the data is represented as a
                    contour plot with multiple levels displayed. If
                    `constraint`, the data is represented as
                    constraints with the invalid region shaded as
                    specified by the `operation` and `value`
                    parameters.
                value
                    Sets the value or values of the constraint
                    boundary. When `operation` is set to one of the
                    comparison values (=,<,>=,>,<=) *value* is
                    expected to be a number. When `operation` is
                    set to one of the interval values
                    ([],(),[),(],][,)(,](,)[) *value* is expected
                    to be an array of two numbers where the first
                    is the lower bound and the second is the upper
                    bound.

        Returns
        -------
        plotly.graph_objs.contour.Contours
        """
        return self['contours']

    @contours.setter
    def contours(self, val):
        self['contours'] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        *scatter* traces also appends customdata items in the markers
        DOM elements
    
        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['customdata']

    @customdata.setter
    def customdata(self, val):
        self['customdata'] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on plot.ly for  customdata .
    
        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['customdatasrc']

    @customdatasrc.setter
    def customdatasrc(self, val):
        self['customdatasrc'] = val

    # dx
    # --
    @property
    def dx(self):
        """
        Sets the x coordinate step. See `x0` for more info.
    
        The 'dx' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dx']

    @dx.setter
    def dx(self, val):
        self['dx'] = val

    # dy
    # --
    @property
    def dy(self):
        """
        Sets the y coordinate step. See `y0` for more info.
    
        The 'dy' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dy']

    @dy.setter
    def dy(self, val):
        self['dy'] = val

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the fill color if `contours.type` is *constraint*.
        Defaults to a half-transparent variant of the line color,
        marker color, or marker line color, whichever is available.
    
        The 'fillcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen
          - A number that will be interpreted as a color
            according to contour.colorscale

        Returns
        -------
        str
        """
        return self['fillcolor']

    @fillcolor.setter
    def fillcolor(self, val):
        self['fillcolor'] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.
    
        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on plot.ly for  hoverinfo .
    
        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hoverinfosrc']

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self['hoverinfosrc'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.contour.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on plot.ly for
                    bgcolor .
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on plot.ly for
                    bordercolor .
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the length (in number of characters) of
                    the trace name in the hover labels for this
                    trace. -1 shows the whole name regardless of
                    length. 0-3 shows the first 0-3 characters, and
                    an integer >3 will show the whole name if it is
                    less than that many characters, but if it is
                    longer, will truncate to `namelength - 3`
                    characters and add an ellipsis.
                namelengthsrc
                    Sets the source reference on plot.ly for
                    namelength .

        Returns
        -------
        plotly.graph_objs.contour.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.
    
        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ids']

    @ids.setter
    def ids(self, val):
        self['ids'] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on plot.ly for  ids .
    
        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['idssrc']

    @idssrc.setter
    def idssrc(self, val):
        self['idssrc'] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.
    
        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['legendgroup']

    @legendgroup.setter
    def legendgroup(self, val):
        self['legendgroup'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.contour.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour level. Has no
                    effect if `contours.coloring` is set to
                    *lines*.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string (*solid*, *dot*, *dash*,
                    *longdash*, *dashdot*, or *longdashdot*) or a
                    dash length list in px (eg *5px,10px,2px,2px*).
                smoothing
                    Sets the amount of smoothing for the contour
                    lines, where *0* corresponds to no smoothing.
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.contour.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # ncontours
    # ---------
    @property
    def ncontours(self):
        """
        Sets the maximum number of contour levels. The actual number of
        contours will be chosen automatically to be less than or equal
        to the value of `ncontours`. Has an effect only if
        `autocontour` is *true* or if `contours.size` is missing.
    
        The 'ncontours' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['ncontours']

    @ncontours.setter
    def ncontours(self, val):
        self['ncontours'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the trace.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. If true, `zmin` will
        correspond to the last color in the array and `zmax` will
        correspond to the first color.
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['reversescale']

    @reversescale.setter
    def reversescale(self, val):
        self['reversescale'] = val

    # selectedpoints
    # --------------
    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.
    
        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['selectedpoints']

    @selectedpoints.setter
    def selectedpoints(self, val):
        self['selectedpoints'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showscale']

    @showscale.setter
    def showscale(self, val):
        self['showscale'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.contour.Stream
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to *50*, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See
                    https://plot.ly/settings for more details.

        Returns
        -------
        plotly.graph_objs.contour.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text elements associated with each z value.
    
        The 'text' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on plot.ly for  text .
    
        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['textsrc']

    @textsrc.setter
    def textsrc(self, val):
        self['textsrc'] = val

    # transpose
    # ---------
    @property
    def transpose(self):
        """
        Transposes the z data.
    
        The 'transpose' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['transpose']

    @transpose.setter
    def transpose(self, val):
        self['transpose'] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['uid']

    @uid.setter
    def uid(self, val):
        self['uid'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        *legendonly*, the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).
    
        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x coordinates.
    
        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # x0
    # --
    @property
    def x0(self):
        """
        Alternate to `x`. Builds a linear space of x coordinates. Use
        with `dx` where `x0` is the starting coordinate and `dx` the
        step.
    
        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x0']

    @x0.setter
    def x0(self, val):
        self['x0'] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If *x* (the default value), the x coordinates
        refer to `layout.xaxis`. If *x2*, the x coordinates refer to
        `layout.xaxis2`, and so on.
    
        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        return self['xaxis']

    @xaxis.setter
    def xaxis(self, val):
        self['xaxis'] = val

    # xcalendar
    # ---------
    @property
    def xcalendar(self):
        """
        Sets the calendar system to use with `x` date data.
    
        The 'xcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['xcalendar']

    @xcalendar.setter
    def xcalendar(self, val):
        self['xcalendar'] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on plot.ly for  x .
    
        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['xsrc']

    @xsrc.setter
    def xsrc(self, val):
        self['xsrc'] = val

    # xtype
    # -----
    @property
    def xtype(self):
        """
        If *array*, the heatmap's x coordinates are given by *x* (the
        default behavior when `x` is provided). If *scaled*, the
        heatmap's x coordinates are given by *x0* and *dx* (the default
        behavior when `x` is not provided).
    
        The 'xtype' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['array', 'scaled']

        Returns
        -------
        Any
        """
        return self['xtype']

    @xtype.setter
    def xtype(self, val):
        self['xtype'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y coordinates.
    
        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # y0
    # --
    @property
    def y0(self):
        """
        Alternate to `y`. Builds a linear space of y coordinates. Use
        with `dy` where `y0` is the starting coordinate and `dy` the
        step.
    
        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y0']

    @y0.setter
    def y0(self, val):
        self['y0'] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If *y* (the default value), the y coordinates
        refer to `layout.yaxis`. If *y2*, the y coordinates refer to
        `layout.yaxis2`, and so on.
    
        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # ycalendar
    # ---------
    @property
    def ycalendar(self):
        """
        Sets the calendar system to use with `y` date data.
    
        The 'ycalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['ycalendar']

    @ycalendar.setter
    def ycalendar(self, val):
        self['ycalendar'] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on plot.ly for  y .
    
        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ysrc']

    @ysrc.setter
    def ysrc(self, val):
        self['ysrc'] = val

    # ytype
    # -----
    @property
    def ytype(self):
        """
        If *array*, the heatmap's y coordinates are given by *y* (the
        default behavior when `y` is provided) If *scaled*, the
        heatmap's y coordinates are given by *y0* and *dy* (the default
        behavior when `y` is not provided)
    
        The 'ytype' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['array', 'scaled']

        Returns
        -------
        Any
        """
        return self['ytype']

    @ytype.setter
    def ytype(self, val):
        self['ytype'] = val

    # z
    # -
    @property
    def z(self):
        """
        Sets the z data.
    
        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # zauto
    # -----
    @property
    def zauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here in `z`) or the bounds set in
        `zmin` and `zmax`  Defaults to `false` when `zmin` and `zmax`
        are set by the user.
    
        The 'zauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['zauto']

    @zauto.setter
    def zauto(self, val):
        self['zauto'] = val

    # zhoverformat
    # ------------
    @property
    def zhoverformat(self):
        """
        Sets the hover text formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. See: https
        ://github.com/d3/d3-format/blob/master/README.md#locale_format
    
        The 'zhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['zhoverformat']

    @zhoverformat.setter
    def zhoverformat(self, val):
        self['zhoverformat'] = val

    # zmax
    # ----
    @property
    def zmax(self):
        """
        Sets the upper bound of the color domain. Value should have the
        same units as in `z` and if set, `zmin` must be set as well.
    
        The 'zmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zmax']

    @zmax.setter
    def zmax(self, val):
        self['zmax'] = val

    # zmin
    # ----
    @property
    def zmin(self):
        """
        Sets the lower bound of the color domain. Value should have the
        same units as in `z` and if set, `zmax` must be set as well.
    
        The 'zmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zmin']

    @zmin.setter
    def zmin(self, val):
        self['zmin'] = val

    # zsrc
    # ----
    @property
    def zsrc(self):
        """
        Sets the source reference on plot.ly for  z .
    
        The 'zsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['zsrc']

    @zsrc.setter
    def zsrc(self, val):
        self['zsrc'] = val

    # type
    # ----
    @property
    def type(self):
        return self._props['type']

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return ''

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If *true*, the number of
            contour levels can be set in `ncontours`. If *false*,
            set the contour level attributes in `contours`.
        colorbar
            plotly.graph_objs.contour.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in.
        contours
            plotly.graph_objs.contour.Contours instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, *scatter* traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        fillcolor
            Sets the fill color if `contours.type` is *constraint*.
            Defaults to a half-transparent variant of the line
            color, marker color, or marker line color, whichever is
            available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.contour.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.contour.Line instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is *true* or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.contour.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on plot.ly for  text .
        transpose
            Transposes the z data.
        uid

        visible
            Determines whether or not this trace is visible. If
            *legendonly*, the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If *x* (the default value), the
            x coordinates refer to `layout.xaxis`. If *x2*, the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        xtype
            If *array*, the heatmap's x coordinates are given by
            *x* (the default behavior when `x` is provided). If
            *scaled*, the heatmap's x coordinates are given by *x0*
            and *dx* (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If *y* (the default value), the
            y coordinates refer to `layout.yaxis`. If *y2*, the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        ytype
            If *array*, the heatmap's y coordinates are given by
            *y* (the default behavior when `y` is provided) If
            *scaled*, the heatmap's y coordinates are given by *y0*
            and *dy* (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .
        """

    def __init__(
        self,
        arg=None,
        autocolorscale=None,
        autocontour=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmin=None,
        zsrc=None,
        **kwargs
    ):
        """
        Construct a new Contour object
        
        The data from which contour lines are computed is set in `z`.
        Data in `z` must be a {2D array} of numbers. Say that `z` has N
        rows and M columns, then by default, these N rows correspond to
        N y coordinates (set in `y` or auto-generated) and the M
        columns correspond to M x coordinates (set in `x` or auto-
        generated). By setting `transpose` to *true*, the above
        behavior is flipped.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Contour
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        autocontour
            Determines whether or not the contour level attributes
            are picked by an algorithm. If *true*, the number of
            contour levels can be set in `ncontours`. If *false*,
            set the contour level attributes in `contours`.
        colorbar
            plotly.graph_objs.contour.ColorBar instance or dict
            with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`zmin` and `zmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the `z` data are filled in.
        contours
            plotly.graph_objs.contour.Contours instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, *scatter* traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        fillcolor
            Sets the fill color if `contours.type` is *constraint*.
            Defaults to a half-transparent variant of the line
            color, marker color, or marker line color, whichever is
            available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.contour.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.contour.Line instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        ncontours
            Sets the maximum number of contour levels. The actual
            number of contours will be chosen automatically to be
            less than or equal to the value of `ncontours`. Has an
            effect only if `autocontour` is *true* or if
            `contours.size` is missing.
        opacity
            Sets the opacity of the trace.
        reversescale
            Reverses the color mapping if true. If true, `zmin`
            will correspond to the last color in the array and
            `zmax` will correspond to the first color.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            plotly.graph_objs.contour.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on plot.ly for  text .
        transpose
            Transposes the z data.
        uid

        visible
            Determines whether or not this trace is visible. If
            *legendonly*, the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If *x* (the default value), the
            x coordinates refer to `layout.xaxis`. If *x2*, the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        xtype
            If *array*, the heatmap's x coordinates are given by
            *x* (the default behavior when `x` is provided). If
            *scaled*, the heatmap's x coordinates are given by *x0*
            and *dx* (the default behavior when `x` is not
            provided).
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If *y* (the default value), the
            y coordinates refer to `layout.yaxis`. If *y2*, the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        ytype
            If *array*, the heatmap's y coordinates are given by
            *y* (the default behavior when `y` is provided) If
            *scaled*, the heatmap's y coordinates are given by *y0*
            and *dy* (the default behavior when `y` is not
            provided)
        z
            Sets the z data.
        zauto
            Determines whether or not the color domain is computed
            with respect to the input data (here in `z`) or the
            bounds set in `zmin` and `zmax`  Defaults to `false`
            when `zmin` and `zmax` are set by the user.
        zhoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. See: https://github.com/d3/d3-format/blob/maste
            r/README.md#locale_format
        zmax
            Sets the upper bound of the color domain. Value should
            have the same units as in `z` and if set, `zmin` must
            be set as well.
        zmin
            Sets the lower bound of the color domain. Value should
            have the same units as in `z` and if set, `zmax` must
            be set as well.
        zsrc
            Sets the source reference on plot.ly for  z .

        Returns
        -------
        Contour
        """
        super(Contour, self).__init__('contour')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Contour 
constructor must be a dict or 
an instance of plotly.graph_objs.Contour"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (contour as v_contour)

        # Initialize validators
        # ---------------------
        self._validators['autocolorscale'
                        ] = v_contour.AutocolorscaleValidator()
        self._validators['autocontour'] = v_contour.AutocontourValidator()
        self._validators['colorbar'] = v_contour.ColorBarValidator()
        self._validators['colorscale'] = v_contour.ColorscaleValidator()
        self._validators['connectgaps'] = v_contour.ConnectgapsValidator()
        self._validators['contours'] = v_contour.ContoursValidator()
        self._validators['customdata'] = v_contour.CustomdataValidator()
        self._validators['customdatasrc'] = v_contour.CustomdatasrcValidator()
        self._validators['dx'] = v_contour.DxValidator()
        self._validators['dy'] = v_contour.DyValidator()
        self._validators['fillcolor'] = v_contour.FillcolorValidator()
        self._validators['hoverinfo'] = v_contour.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_contour.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_contour.HoverlabelValidator()
        self._validators['ids'] = v_contour.IdsValidator()
        self._validators['idssrc'] = v_contour.IdssrcValidator()
        self._validators['legendgroup'] = v_contour.LegendgroupValidator()
        self._validators['line'] = v_contour.LineValidator()
        self._validators['name'] = v_contour.NameValidator()
        self._validators['ncontours'] = v_contour.NcontoursValidator()
        self._validators['opacity'] = v_contour.OpacityValidator()
        self._validators['reversescale'] = v_contour.ReversescaleValidator()
        self._validators['selectedpoints'
                        ] = v_contour.SelectedpointsValidator()
        self._validators['showlegend'] = v_contour.ShowlegendValidator()
        self._validators['showscale'] = v_contour.ShowscaleValidator()
        self._validators['stream'] = v_contour.StreamValidator()
        self._validators['text'] = v_contour.TextValidator()
        self._validators['textsrc'] = v_contour.TextsrcValidator()
        self._validators['transpose'] = v_contour.TransposeValidator()
        self._validators['uid'] = v_contour.UidValidator()
        self._validators['visible'] = v_contour.VisibleValidator()
        self._validators['x'] = v_contour.XValidator()
        self._validators['x0'] = v_contour.X0Validator()
        self._validators['xaxis'] = v_contour.XAxisValidator()
        self._validators['xcalendar'] = v_contour.XcalendarValidator()
        self._validators['xsrc'] = v_contour.XsrcValidator()
        self._validators['xtype'] = v_contour.XtypeValidator()
        self._validators['y'] = v_contour.YValidator()
        self._validators['y0'] = v_contour.Y0Validator()
        self._validators['yaxis'] = v_contour.YAxisValidator()
        self._validators['ycalendar'] = v_contour.YcalendarValidator()
        self._validators['ysrc'] = v_contour.YsrcValidator()
        self._validators['ytype'] = v_contour.YtypeValidator()
        self._validators['z'] = v_contour.ZValidator()
        self._validators['zauto'] = v_contour.ZautoValidator()
        self._validators['zhoverformat'] = v_contour.ZhoverformatValidator()
        self._validators['zmax'] = v_contour.ZmaxValidator()
        self._validators['zmin'] = v_contour.ZminValidator()
        self._validators['zsrc'] = v_contour.ZsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('autocolorscale', None)
        self.autocolorscale = autocolorscale if autocolorscale is not None else _v
        _v = arg.pop('autocontour', None)
        self.autocontour = autocontour if autocontour is not None else _v
        _v = arg.pop('colorbar', None)
        self.colorbar = colorbar if colorbar is not None else _v
        _v = arg.pop('colorscale', None)
        self.colorscale = colorscale if colorscale is not None else _v
        _v = arg.pop('connectgaps', None)
        self.connectgaps = connectgaps if connectgaps is not None else _v
        _v = arg.pop('contours', None)
        self.contours = contours if contours is not None else _v
        _v = arg.pop('customdata', None)
        self.customdata = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self.customdatasrc = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('dx', None)
        self.dx = dx if dx is not None else _v
        _v = arg.pop('dy', None)
        self.dy = dy if dy is not None else _v
        _v = arg.pop('fillcolor', None)
        self.fillcolor = fillcolor if fillcolor is not None else _v
        _v = arg.pop('hoverinfo', None)
        self.hoverinfo = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoverinfosrc', None)
        self.hoverinfosrc = hoverinfosrc if hoverinfosrc is not None else _v
        _v = arg.pop('hoverlabel', None)
        self.hoverlabel = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('ids', None)
        self.ids = ids if ids is not None else _v
        _v = arg.pop('idssrc', None)
        self.idssrc = idssrc if idssrc is not None else _v
        _v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup if legendgroup is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('ncontours', None)
        self.ncontours = ncontours if ncontours is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('reversescale', None)
        self.reversescale = reversescale if reversescale is not None else _v
        _v = arg.pop('selectedpoints', None)
        self.selectedpoints = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self.showlegend = showlegend if showlegend is not None else _v
        _v = arg.pop('showscale', None)
        self.showscale = showscale if showscale is not None else _v
        _v = arg.pop('stream', None)
        self.stream = stream if stream is not None else _v
        _v = arg.pop('text', None)
        self.text = text if text is not None else _v
        _v = arg.pop('textsrc', None)
        self.textsrc = textsrc if textsrc is not None else _v
        _v = arg.pop('transpose', None)
        self.transpose = transpose if transpose is not None else _v
        _v = arg.pop('uid', None)
        self.uid = uid if uid is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v
        _v = arg.pop('x', None)
        self.x = x if x is not None else _v
        _v = arg.pop('x0', None)
        self.x0 = x0 if x0 is not None else _v
        _v = arg.pop('xaxis', None)
        self.xaxis = xaxis if xaxis is not None else _v
        _v = arg.pop('xcalendar', None)
        self.xcalendar = xcalendar if xcalendar is not None else _v
        _v = arg.pop('xsrc', None)
        self.xsrc = xsrc if xsrc is not None else _v
        _v = arg.pop('xtype', None)
        self.xtype = xtype if xtype is not None else _v
        _v = arg.pop('y', None)
        self.y = y if y is not None else _v
        _v = arg.pop('y0', None)
        self.y0 = y0 if y0 is not None else _v
        _v = arg.pop('yaxis', None)
        self.yaxis = yaxis if yaxis is not None else _v
        _v = arg.pop('ycalendar', None)
        self.ycalendar = ycalendar if ycalendar is not None else _v
        _v = arg.pop('ysrc', None)
        self.ysrc = ysrc if ysrc is not None else _v
        _v = arg.pop('ytype', None)
        self.ytype = ytype if ytype is not None else _v
        _v = arg.pop('z', None)
        self.z = z if z is not None else _v
        _v = arg.pop('zauto', None)
        self.zauto = zauto if zauto is not None else _v
        _v = arg.pop('zhoverformat', None)
        self.zhoverformat = zhoverformat if zhoverformat is not None else _v
        _v = arg.pop('zmax', None)
        self.zmax = zmax if zmax is not None else _v
        _v = arg.pop('zmin', None)
        self.zmin = zmin if zmin is not None else _v
        _v = arg.pop('zsrc', None)
        self.zsrc = zsrc if zsrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'contour'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='contour'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
