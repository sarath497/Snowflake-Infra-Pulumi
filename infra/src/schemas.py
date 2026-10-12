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

raw = snowflake.Schema(
    "raw",
    database="MYMOBILITY_OPS",
    name="RAW"
)

curated = snowflake.Schema(
    "curated",
    database="MYMOBILITY_OPS",
    name="CURATED"
)

published = snowflake.Schema(
    "published",
    database="MYMOBILITY_OPS",
    name="PUBLISHED"
)

