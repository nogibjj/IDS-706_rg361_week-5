"""
Query Scripts Using SQLite and Python which can be exceuted via CLI
"""

# Import libraries
import sys
sys.path.insert(0, "./mylib")
import argparse


# Import Custom Libraries functions
#from mylib.data_csv import create_data, delete_data
from mylib.create import create_db
from mylib.read import read_db
from mylib.update import update_db
from mylib.delete import delete_record


def handle_arguments(args):
    """To Handle initial arguments"""
    parser = argparse.ArgumentParser(description="CRUD Operations on SQLite DB")
    parser.add_argument(
        "action",
        choices=[
            "create",
            "read",
            "update",
            "delete",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)
    if args.action == "create":
        parser.add_argument("db_name",type=str, nargs='?', default="Master.db")
        parser.add_argument("dataset_name",type=str, nargs='?', default="Master.csv")
        parser.add_argument("auto",type=str, nargs='?', default="True")

    elif args.action in ["read", "update", "delete"]:
        parser.add_argument("db_name",type=str, nargs='?',default="Master.db")
        parser.add_argument("table_name",type=str, nargs='?',default="Master")
        parser.add_argument("query",type=str, nargs='?',default=None)

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """To call other fucntions based on the arguments"""

    args = handle_arguments(sys.argv[1:])

    if args.action == "create":
        print("creating...")
        create_db(args.db_name, args.dataset_name, args.auto)
        print("created")
    elif args.action == "read":
        print("processing...")
        print(read_db(args.db_name, args.table_name, args.query))
        print("processed")
    elif args.action == "update":
        print("processing...")
        print(update_db(args.db_name, args.table_name, args.query))
        print("processed")
    elif args.action == "delete":
        print("processing...")
        print(delete_record(args.db_name, args.table_name, args.query))
        print("processed")
    else:
        print(f"Unknown Input: {args.action}")


if __name__ == "__main__":
    main()
