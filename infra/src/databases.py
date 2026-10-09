import pulumi_snowflake as snowflake

sales_db = snowflake.Database(
    "sales-db",
    name="SALES_DB",
    comment="Managed by Pulumi"
)