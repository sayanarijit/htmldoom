<div><h1 align="center">htmldoom</h1><p align="center">Write safer and cleaner HTML using Python</p><p align="center"><span><a href="https://pypi.org/project/htmldoom"><img src="https://img.shields.io/pypi/v/htmldoom.svg" alt="PyPI version" /></a></span>&nbsp;<span><a href="https://pypi.org/project/htmldoom"><img src="https://img.shields.io/pypi/pyversions/htmldoom.svg" alt="PyPI pyversions" /></a></span>&nbsp;<span><a href="https://travis-ci.org/sayanarijit/htmldoom"><img src="https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master" alt="Build Status" /></a></span>&nbsp;<span><a href="https://codecov.io/gh/sayanarijit/htmldoom"><img src="https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg" alt="codecov" /></a></span>&nbsp;<span><a href="https://github.com/python/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" /></a></span></p><p><h2>Usage</h2><p><pre>&gt;&gt;&gt; from htmldoom import elements as e
&gt;&gt;&gt; 
&gt;&gt;&gt; e.P(style=e.style(color=&quot;red&quot;))(&quot;This is a paragraph&quot;)
&lt;p style=&quot;color:&#x27;red&#x27;;&quot;&gt;This is a paragraph&lt;/p&gt;</pre></p><p><pre>&gt;&gt;&gt; from htmldoom import elements as e
&gt;&gt;&gt; from htmldoom.layouts import BaseLayout
&gt;&gt;&gt; 
&gt;&gt;&gt; class MyLayout(BaseLayout):
...     @property
...     def title(self) -&gt; e.Title:
...         return e.Title()(self.data[&quot;title&quot;])
...     @property
...     def body(self) -&gt; e.Body:
...         return e.Body()(f&quot;Welcome {self.data[&#x27;user&#x27;][&#x27;name&#x27;]}&quot;)

... 
&gt;&gt;&gt; MyLayout({&quot;title&quot;: &quot;foo&quot;, &quot;user&quot;: {&quot;name&quot;: &quot;bar&quot;}})
&lt;!DOCTYPE html&gt;
&lt;html&gt;&lt;head&gt;&lt;title&gt;foo&lt;/title&gt;&lt;/head&gt;&lt;body&gt;Welcome bar&lt;/body&gt;&lt;/html&gt;</pre></p><p><a href="https://github.com/sayanarijit/htmldoom/tree/master/examples">Find more examples here</a></p></p><p><h2>Benchmarks</h2><p>Very basic benchmark done using <a href="https://github.com/sayanarijit/htmldoom/blob/master/benchmark/general.py">this script</a> and IPython</p><h3>htmldoom</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/6dmd4r7lgoqu9wrv4wr9.png" alt="htmldoom stats" /><h3>Jinja2</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/hvvuvybfk5jved6trinr.png" alt="Jinja2 stats" /><h3>Mako</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/xyzdag8221qzoohz1tx9.png" alt="Mako stats" /><h3>Chameleon</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/0j49ln7pa62ivhqzkkuq.png" alt="Chameleon stats" /><h3>Conclusion</h3><p>htmldoom performs best upto a certain number of loops which is generally high enough. These measurements are very naive and shows very basic information.</p></p><p><h2>Contributing</h2><p>Check out the <a href="https://github.com/sayanarijit/htmldoom/tree/master/CONTRIBUTING.md"> contributing guidelines.</a></p></p></div>
