__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

database_path = snakemake.params.get("database_path", None)
if database_path is None:
    raise Exception("Input error, missing database_path")

build_version = snakemake.params.get("build_version", None)
if build_version is None:
    raise Exception("Input error, missing build_version")

protocol = snakemake.params.get("protocols", None)
if protocol is None:
    raise Exception("Input error, missing protocols")

operation = snakemake.params.get("operations", None)
if operation is None:
    raise Exception("Input error, missing operation")

arguments = snakemake.params.get("arguments", None)
if arguments is None:
    arguments = ""
else:
    arguments = "-arg " + arguments

na_string = snakemake.params.get("na_string", ".")

extra = snakemake.params.get("extra", "")

shell("table_annovar.pl "
      " {snakemake.input}"
      " -out {snakemake.output}"
      " {database_path}"
      " -buildver {build_version}"
      " -protocol {protocol}"
      " -operation {operation}"
      " -nastring {na_string}"
      " {arguments} "
      " {extra}"
      " -vcfinput"
      " {log} &&"
      " cp {snakemake.output}.{build_version}_multianno.vcf {snakemake.output}")
