### Rendered pages

```bash
PYTHONPATH=$PWD python jinja2/render.py

PYTHONPATH=$PWD python htmldoom/render.py
```

### Benchmarks

```python

In [1]: from jinja2_pages.render import render as jinja2_renderer

In [2]: from htmldoom_pages.render import render as htmldoom_renderer

In [3]: %timeit jinja2_renderer(10)
102 µs ± 2.45 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [4]: %timeit htmldoom_renderer(10)
85.6 µs ± 1.53 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [5]: %timeit jinja2_renderer(50)
407 µs ± 3.37 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [6]: %timeit htmldoom_renderer(50)
403 µs ± 9.25 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [7]: %timeit jinja2_renderer(100)
776 µs ± 4.78 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [8]: %timeit htmldoom_renderer(100)
794 µs ± 6.12 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [9]: %timeit jinja2_renderer(500)
3.81 ms ± 107 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [10]: %timeit htmldoom_renderer(500)
3.97 ms ± 43.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Please help improving the benchmark tests
