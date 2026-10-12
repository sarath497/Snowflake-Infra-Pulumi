import pulumi_snowflake as snowflake

#Warehouse usage grant
warehouse_usage = snowflake.GrantPrivilegesToAccountRole(
    "warehouse_usage",
    account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
    privileges=["USAGE"],
    on_account_object={
        "object_type": "WAREHOUSE",
        "object_name": "ZB_COMMON_XS_01"
    }
)

#Database usage Grants
database_usage = snowflake.GrantPrivilegesToAccountRole(
    "database_usage",
    account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
    privileges=["USAGE"],
    on_account_object={
        "object_type": "DATABASE",
        "object_name": "MYMOBILITY_OPS"
    }
)


schemas = [
    "RAW",
    "CURATED",
    "PUBLISHED"
]

#Schema usage grants
for schema in schemas:
    snowflake.GrantPrivilegesToAccountRole(
        f"{schema.lower()}_schema_usage",
        account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
        privileges=["USAGE"],
        on_schema={
            "schema_name": f"MYMOBILITY_OPS.{schema}"
        }
    )

# Table creation grants on three schemas
for schema in schemas:
    snowflake.GrantPrivilegesToAccountRole(
        f"{schema.lower()}_create_table",
        account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
        privileges=["CREATE TABLE"],
        on_schema={
            "schema_name": f"MYMOBILITY_OPS.{schema}"
        }
    )
    
#View creating permission
for schema in schemas:
    snowflake.GrantPrivilegesToAccountRole(
        f"{schema.lower()}_create_view",
        account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
        privileges=["CREATE VIEW"],
        on_schema={
            "schema_name": f"MYMOBILITY_OPS.{schema}"
        }
    )
    
#DML access on existing tables
for schema in schemas:
    snowflake.GrantPrivilegesToAccountRole(
        f"{schema.lower()}_all_table_dml",
        account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
        privileges=[
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        on_schema_object={
            "all": {
                "object_type_plural": "TABLES",
                "in_schema": f"MYMOBILITY_OPS.{schema}"
            }
        }
    )
    
#future DML access 
for schema in schemas:
    snowflake.GrantPrivilegesToAccountRole(
        f"{schema.lower()}_future_table_dml",
        account_role_name="SF_UDP_AMERDEV01_MYMOBILITY_OPS_WRITE",
        privileges=[
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        on_schema_object={
            "future": {
                "object_type_plural": "TABLES",
                "in_schema": f"MYMOBILITY_OPS.{schema}"
            }
        }
    )