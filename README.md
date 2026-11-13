# Cutest picture — make.fun entry

A tiny round baby penguin with big dark eyes hugging a small yellow star
plushie, on a soft pastel pink background. The subject fills the frame and
still reads at small size.

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
