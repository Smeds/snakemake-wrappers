__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

vcf_input = snakemake.input[0]

if vcf_input is None:
    raise ValueError("Missing vcf input file!")
elif not len(snakemake.input) == 1:
    raise ValueError("Only expecting one input file: " + str(snakemake.input) + "!")

vcf_output = snakemake.output[0]

if vcf_output is None:
    raise ValueError("Missing output file")
elif not len(snakemake.output) == 1:
    raise ValueError("Only expecting one output file: " + str(output_file) + "!")

count_variants = 0
with open(vcf_input) as vcf:
    for line in vcf:
        if not line.startswith("#"):
            count_variants = count_variants + 1

if count_variants > 0:
    shell(
        "lofreq2_indel_ovlp.py "
        " {extra}"
        " {vcf_input} > {vcf_output}"
        " {log}")
else:
    shell("cp {vcf_input} {vcf_output}")
