
import json

from nexus_ai.system_info import get_system_report


def main():
    print("=" * 50)
    print("          NEXUS OS - SYSTEM INTELLIGENCE")
    print("=" * 50)

    report = get_system_report()

    print(json.dumps(report, indent=4))

    print("\nNEXUS system inspection completed.")


if __name__ == "__main__":
    main()
