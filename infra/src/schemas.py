import pulumi_snowflake as snowflake

raw_schema = snowflake.Schema(
    "raw-schema",
    database="SALES_DB",
    name="RAW"
)

curated_schema = snowflake.Schema(
    "curated-schema",
    database="SALES_DB",
    name="CURATED"
)