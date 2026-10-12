import pulumi_snowflake as snowflake

ZB_COMMON_XS_01 = snowflake.Warehouse(
    "ZB_COMMON_XS_01",
    name="ZB_COMMON_XS_01",
    warehouse_size="XSMALL",
    auto_suspend=60,
    auto_resume=True
)