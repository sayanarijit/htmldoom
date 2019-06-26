<div><h1 align="center">htmldoom</h1><p align="center">Write safer and cleaner HTML using Python</p><p align="center"><span><a href="https://pypi.org/project/htmldoom"><img src="https://img.shields.io/pypi/v/htmldoom.svg" alt="PyPI version" /></a></span>&nbsp;<span><a href="https://pypi.org/project/htmldoom"><img src="https://img.shields.io/pypi/pyversions/htmldoom.svg" alt="PyPI version" /></a></span>&nbsp;<span><a href="https://travis-ci.org/sayanarijit/htmldoom"><img src="https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master" alt="Build Status" /></a></span>&nbsp;<span><a href="https://codecov.io/gh/sayanarijit/htmldoom"><img src="https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg" alt="codecov" /></a></span>&nbsp;<span><a href="https://github.com/python/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" /></a></span></p><p><h2>Usage</h2><p><h2>A basic tag</h2><pre>&gt;&gt;&gt; from htmldoom import elements as e
&gt;&gt;&gt; 
&gt;&gt;&gt; e.P(style=e.style(color=&quot;red&quot;))(&quot;This is a paragraph&quot;)
&lt;p style=&quot;color:&#x27;red&#x27;;&quot;&gt;This is a paragraph&lt;/p&gt;</pre></p><p><h2>A builtin layout</h2><pre>&gt;&gt;&gt; from htmldoom import elements as e
&gt;&gt;&gt; from htmldoom.layouts import BaseLayout
&gt;&gt;&gt; 
&gt;&gt;&gt; class MyLayout(BaseLayout):
... 
...     @property
...     def title(self) -&gt; e.Title:
...         return e.Title()(self[&quot;title&quot;])
... 
...     @property
...     def body(self) -&gt; e.Body:
...         return e.Body()(f&quot;Welcome {self[&#x27;user&#x27;][&#x27;name&#x27;]}&quot;)
... 
&gt;&gt;&gt; MyLayout({&quot;title&quot;: &quot;foo&quot;, &quot;user&quot;: {&quot;name&quot;: &quot;bar&quot;}})
&lt;!DOCTYPE html&gt;
&lt;html&gt;&lt;head&gt;&lt;title&gt;foo&lt;/title&gt;&lt;/head&gt;&lt;body&gt;Welcome bar&lt;/body&gt;&lt;/html&gt;</pre></p><p><h2>A functional style foreach loop with a switch case</h2><pre>&gt;&gt;&gt; from htmldoom import elements as e
&gt;&gt;&gt; from htmldoom import functions as fn
&gt;&gt;&gt; 
&gt;&gt;&gt; fn.foreach([&quot;good&quot;, &quot;bad&quot;, &quot;evil&quot;])(
...     lambda x: fn.switch({
...         x == &quot;good&quot;: lambda: e.Span(style=&quot;color: green&quot;)(f&quot;this is {x}&quot;),
...         x == &quot;bad&quot;: lambda: e.Span(style=&quot;color: yellow&quot;)(f&quot;this is {x}&quot;),
...         fn.Case.DEFAULT: lambda: e.Span(style=&quot;color: red&quot;)(f&quot;this is {x}&quot;),
...     })
... )
(&lt;span style=&quot;color: green&quot;&gt;this is good&lt;/span&gt;,
 &lt;span style=&quot;color: yellow&quot;&gt;this is bad&lt;/span&gt;,
 &lt;span style=&quot;color: red&quot;&gt;this is evil&lt;/span&gt;)
</pre></p><p><a href="https://github.com/sayanarijit/htmldoom/tree/master/examples"><b>Find more examples here</b></a></p></p><p><h2>Q/A</h2><h3>What is the goal here?</h3><p>The primary goal is to make writing HTML cleaner, easier, safer and intuitive using Python.</p><h3>What about performance?</h3><p>Although performance is not the primary goal here, it should not be a roadblock. htmldoom is copying the syntax and properties of <a href="https://elm-lang.org">elm</a>, an existing fast and purely functional programming language that specializes in rendering HTML in virtual doms. Elm does all the optimisation internally which I&#x27;m sure can be implemented in Python to a great extent.<br />All the elements and attributes in htmldoom are supposed to be immutable (unless you want to hack it for some reason). Being immutable enables them to be cachable and sharable making use of the <a href="https://en.wikipedia.org/wiki/Flyweight_pattern">flyweight pattern</a>, thus improving the speed of rendering.<br />Furthermore, if we follow the <a href="https://developers.google.com/web/tools/lighthouse/audits/dom-size">the DOM size recommendations</a>, i.e.<ul><li>less than 1500 nodes total.</li><li>maximum depth of 32 nodes.</li><li>no parent node with more than 60 child nodes.</li></ul> htmldoom performs really well (refer to the <a href="#benchmarks">benchmarks</a>).</p></p><p><h2>Plugins and ecosystem</h2><p><ul><li><a href="https://github.com/sayanarijit/moodlmth"><b>moodlmth</b></a><span>: Convert raw HTML pages into python source code</span></li></ul><ul><li><a href="https://github.com/sayanarijit/pyramid_htmldoom"><b>pyramid_htmldoom</b></a><span>: htmldoom rendering library plugin for Pyramid</span></li></ul></p></p><p><h2>Benchmarks</h2><p>Very basic benchmark done using <a href="https://github.com/sayanarijit/htmldoom/blob/master/benchmark/general.py">this script</a> and IPython</p><p><h3>htmldoom</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/6dmd4r7lgoqu9wrv4wr9.png" alt="htmldoom stats" /></p><p><h3>Jinja2</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/hvvuvybfk5jved6trinr.png" alt="Jinja2 stats" /></p><p><h3>Mako</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/xyzdag8221qzoohz1tx9.png" alt="Mako stats" /></p><p><h3>Chameleon</h3><img src="https://thepracticaldev.s3.amazonaws.com/i/0j49ln7pa62ivhqzkkuq.png" alt="Chameleon stats" /></p><h3>Conclusion</h3><p>htmldoom performs best upto a certain number of loops which is generally high enough.<br />NOTE: These measurements are very naive and shows very basic information.</p></p><p><h2>Contributing</h2><p>Check out the <a href="https://github.com/sayanarijit/htmldoom/tree/master/CONTRIBUTING.md"> contributing guidelines.</a></p></p></div>
