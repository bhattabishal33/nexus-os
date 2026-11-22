
import unittest

from nexus_ai.system_info import (
    get_os_info,
    get_cpu_info,
    get_memory_info,
    get_disk_info,
    get_system_report,
)


class TestSystemInfo(unittest.TestCase):

    def test_os_info(self):
        result = get_os_info()

        self.assertIn("system", result)
        self.assertIn("architecture", result)
        self.assertIn("hostname", result)

    def test_cpu_info(self):
        result = get_cpu_info()

        self.assertIn("processor", result)
        self.assertGreater(result["logical_cores"], 0)

    def test_memory_info(self):
        result = get_memory_info()

        if result.get("available"):
            self.assertGreater(result["total_mb"], 0)
            self.assertGreaterEqual(result["available_mb"], 0)

    def test_disk_info(self):
        result = get_disk_info()

        self.assertGreater(result["total_gb"], 0)
        self.assertGreaterEqual(result["free_gb"], 0)

    def test_complete_system_report(self):
        result = get_system_report()

        self.assertIn("operating_system", result)
        self.assertIn("cpu", result)
        self.assertIn("memory", result)
        self.assertIn("disk", result)


if __name__ == "__main__":
    unittest.main()
