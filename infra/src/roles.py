import pulumi_snowflake as snowflake

SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE = snowflake.AccountRole(
    "SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
    name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE"
)