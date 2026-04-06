import logging

# Konfigurasi logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='generated_logs.log',
    filemode='w'
)

# Buat instance logger
logger = logging.getLogger('CustomLogger')

# Generate berbagai log
logger.debug("Debug message for troubleshooting")
logger.info("Info message for system events")
logger.warning("Warning: Disk space is running low")
logger.error("Error encountered while connecting to the database")
logger.critical("Critical: System shutdown initiated due to overheating")