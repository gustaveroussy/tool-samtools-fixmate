"""Snakemake wrapper for running samtools fixmate."""

__author__ = "Bastien Job"
__copyright__ = "Copyright 2019, Bastien Job"
__email__ = "bastien.job@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam_input = snakemake.input.bam
bam_output = snakemake.output.bam
extra = snakemake.params.get("extra", "")

if not snakemake.output[0].endswith(".bam"):
    raise Exception("output file should be a BAM")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("samtools fixmate -m "
        "{extra} "
        "{bam_input}  "
        "{bam_output} "
        "{log}")
