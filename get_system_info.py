import platform
def get_system_info():
  """Gets basic system information using platform module."""

  # Get system information
  os = platform.system()
  os_version = platform.version()
  architecture = platform.architecture()
  processor = platform.processor()

  # Print information
  print(f"Operating System: {os} {os_version}")
  print(f"Architecture: {architecture}")
  print(f"Processor: {processor}")

if __name__ == "__main__":
  get_system_info()

