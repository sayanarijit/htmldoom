### Rendered pages

```bash
PYTHONPATH=$PWD python jinja2/render.py

PYTHONPATH=$PWD python htmldoom/render.py
```

### Benchmarks

```python
In [1]: from htmldoom_pages.render import render as htmldoom_renderer

In [2]: from jinja2_pages.render import render as jinja2_renderer

In [3]: %timeit htmldoom_renderer(50)
389 µs ± 4.36 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [4]: %timeit jinja2_renderer(50)
411 µs ± 4.54 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [5]: %timeit htmldoom_renderer(100)
760 µs ± 4.84 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [6]: %timeit jinja2_renderer(100)
784 µs ± 3.34 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

In [7]: %timeit htmldoom_renderer(500)
3.78 ms ± 24.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [8]: %timeit jinja2_renderer(500)
3.95 ms ± 86.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

Please help improving the benchmark tests
