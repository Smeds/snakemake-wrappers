__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

shell(
    "(cnvkit.py scatter "
    "-s {snakemake.input.cns} "
    "{snakemake.input.cnr} "
    "-o {snakemake.output} "
    "{extra}) "
    "{log}"
)
