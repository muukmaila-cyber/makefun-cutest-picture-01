# Cutest picture — make.fun entry

A tiny cream kitten with huge round eyes hugging a fluffy yellow chick,
both cuddling close with soft warm light, on a plain warm cream background.
The pair fills the frame and still reads at small size.

`main.py` (stdlib only, no network) copies the bundled `picture.jpg` to
`/output/entry.png` and verifies it: JPEG magic bytes, at most 1 MiB,
at most 1024×1024, output byte-identical to the source. Run it twice and
the outputs are identical.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
