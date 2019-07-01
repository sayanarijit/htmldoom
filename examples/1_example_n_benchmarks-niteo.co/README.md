### Rendered pages

```bash
PYTHONPATH=$PWD python jinja2/render.py

PYTHONPATH=$PWD python htmldoom/render.py
```

### Benchmarks

```python
In [1]: from jinja2_pages.render import render as jinja2_renderer

In [2]: from htmldoom_pages.render import render as htmldoom_renderer

In [3]: %timeit jinja2_renderer()
29.7 µs ± 125 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [4]: %timeit htmldoom_renderer()
13.4 µs ± 38.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

Please help improving the benchmark tests
