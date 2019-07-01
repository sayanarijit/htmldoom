<h1 align="center">htmldoom</h1><p align="center">An intuitive, high performance HTML rendering framework</p><p align="center"><span><a href="https://pypi.org/project/htmldoom"><img src="https://img.shields.io/pypi/v/htmldoom.svg" alt="PyPI version" /></a></span>&nbsp;<span><a href="https://pypi.org/project/htmldoom"><img src="https://img.shields.io/pypi/pyversions/htmldoom.svg" alt="PyPI version" /></a></span>&nbsp;<span><a href="https://travis-ci.org/sayanarijit/htmldoom"><img src="https://travis-ci.org/sayanarijit/htmldoom.svg?branch=master" alt="Build Status" /></a></span>&nbsp;<span><a href="https://codecov.io/gh/sayanarijit/htmldoom"><img src="https://codecov.io/gh/sayanarijit/htmldoom/branch/master/graph/badge.svg" alt="codecov" /></a></span>&nbsp;<span><a href="https://github.com/python/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" /></a></span></p><h2>Usage</h2><p><h2>A basic tag</h2><pre>&gt;&gt;&gt; from htmldoom import render, elements as e
&gt;&gt;&gt; 
&gt;&gt;&gt; print(render(
...     e.textarea(&quot;required&quot;, class_=&quot;input&quot;)(&quot;text&quot;)
... ))
&lt;textarea required class=&quot;input&quot;&gt;text&lt;/textarea&gt;</pre></p><p><h2>A fast dynamic elements rendering mechanism</h2><p>Choose whichever syntax suits you:</p><h3>Syntax 1</h3><pre>&gt;&gt;&gt; from htmldoom import renders, elements as e
&gt;&gt;&gt; 
&gt;&gt;&gt; @renders(
...     e.p()(&quot;{x}&quot;),
...     e.p()(&quot;another {x}&quot;),
... )
... def render_paras(data: dict) -&gt; dict:
...     return {&quot;x&quot;: data[&quot;x&quot;]}
&gt;&gt;&gt; 
&gt;&gt;&gt; render_paras({&quot;x&quot;: &quot;awesome paragraph&quot;})
&lt;p&gt;awesome paragraph&lt;/p&gt;&lt;p&gt;another awesome paragraph&lt;/p&gt;
</pre><h3>Syntax 2</h3><pre>&gt;&gt;&gt; from htmldoom import renders, elements as e
&gt;&gt;&gt; 
&gt;&gt;&gt; render_paras = renders(
...     e.p()(&quot;{x}&quot;),
...     e.p()(&quot;another {x}&quot;),
... )(lambda data: {&quot;x&quot;: data[&quot;x&quot;]})
&gt;&gt;&gt; 
&gt;&gt;&gt; render_paras({&quot;x&quot;: &quot;awesome paragraph&quot;})
&lt;p&gt;awesome paragraph&lt;/p&gt;&lt;p&gt;another awesome paragraph&lt;/p&gt;
</pre><p><b>NOTE: </b>This mechanism compiles the template when the file loads and reuse it.<br /><pre>renders( -- compile-time code -- )( -- runtime code -- )</pre><br />The more execution you move from runtime to compile-time, the faster it gets.<br />If you properly use this mechanism and refractor your dynamic pages into smaller components, it will surpass the performance of traditional template rendering engines.</p><p><b>WARNING: </b>It performs a <code>&quot;{rendered_elements}&quot;.format(**returned_data)</code>. So be careful about where you put which code.</p></p><p><h2>A functional style foreach loop with a switch case</h2><pre>&gt;&gt;&gt; from htmldoom import elements as e
&gt;&gt;&gt; from htmldoom import functions as fn
&gt;&gt;&gt; 
&gt;&gt;&gt; tuple(fn.foreach([&quot;good&quot;, &quot;bad&quot;, &quot;evil&quot;])(
...     lambda x: fn.switch({
...         x == &quot;good&quot;: lambda: e.span(style=&quot;color: green&quot;)(f&quot;this is {x}&quot;),
...         x == &quot;bad&quot;: lambda: e.span(style=&quot;color: yellow&quot;)(f&quot;this is {x}&quot;),
...         x == &quot;evil&quot;: lambda: e.span(style=&quot;color: red&quot;)(f&quot;this is {x}&quot;),
...         fn.Case.DEFAULT: lambda: fn.Error.throw(ValueError(x)),
...     })
... ))
(b&#x27;&lt;span style=&quot;color: green&quot;&gt;this is good&lt;/span&gt;&#x27;,
 b&#x27;&lt;span style=&quot;color: yellow&quot;&gt;this is bad&lt;/span&gt;&#x27;,
 b&#x27;&lt;span style=&quot;color: red&quot;&gt;this is evil&lt;/span&gt;&#x27;)
</pre></p><p><a href="https://github.com/sayanarijit/htmldoom/tree/master/examples"><b>Find more examples here</b></a></p><p><h2>Q/A</h2><h3>What is the goal here?</h3><p>The primary goal is to make writing dynamic HTML pages cleaner, easier, safer and intuitive in Python.</p><h3>What about performance?</h3><p>Although performance is not the primary goal here, it should not be a roadblock. htmldoom is copying the syntax and some of the rendering properties of <a href="https://elm-lang.org">elm</a>, an existing fast and purely functional programming language that specializes in rendering HTML in virtual doms. Elm does all the optimisation internally, which I believe can be implemented in Python to a great extent.</p><h3>Still worried about performance. Is there any benchmark?</h3><p>Basic benchmarks are done and it shows that htmldoom performs better than traditional rendering engines without explicitly making any optimisation.<br /><a href="https://github.com/sayanarijit/htmldoom/blob/master/examples"><b>Refer to the benchmarks here.</b></a></p></p><p><h2>Plugins and ecosystem</h2><p><ul><li><a href="https://github.com/sayanarijit/moodlmth"><b>moodlmth</b></a><span>: Convert raw HTML pages into python source code</span></li></ul><ul><li><a href="https://github.com/sayanarijit/pyramid_htmldoom"><b>pyramid_htmldoom</b></a><span>: htmldoom rendering library plugin for Pyramid</span></li></ul></p></p><p><h2>Contributing</h2><p>Check out the <a href="https://github.com/sayanarijit/htmldoom/tree/master/CONTRIBUTING.md"> contributing guidelines.</a></p></p>
