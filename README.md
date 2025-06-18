# ScheduleManager

ScheduleManager is a simple Python program for managing appointments, designed for medical offices, professional studios, or anyone who needs to keep track of client meetings.

> **This software was developed for educational purposes.**

## Features

- **Add new appointments:** name, surname, date/time (ISO format), short description.
- **View appointments:** list with progressive number, customer name, formatted date/time, remaining time.
- **Compare appointments:** select two appointments and compare which comes first and the time difference.
- **Reschedule appointments:** add/subtract days and minutes to an appointment.
- **Search by customer name:** lexicographical search among existing appointments.
- **Simple textual interface:** interactive menu via terminal.

## Requirements

- Python 3.7 or above  
  (The program uses the standard `datetime` library.)

## Installation and Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Glitch-dn/Rubrica_appuntamenti.git
    cd ScheduleManager
    ```

2. **Start the program:**
    ```bash
    scheduleManager.py
    ```

   > If you have multiple Python versions installed, you may need to use `python3`.

## Usage

When started, the program displays a menu with the following options:

1. Add new appointment  
2. View appointments  
3. Compare two appointments  
4. Reschedule an appointment  
5. Search appointment by customer name  
6. Exit  

Follow the on-screen instructions to enter the required data.

## Notes

- The program **does not save data to file**: all appointments are lost when the application is closed.
- The date/time must be entered in ISO format, for example: `2025-06-20 14:30`.

## Contributing

Pull requests are welcome!  
To report issues or suggest improvements, use the Issues section of the repository.

---

Developed by [Glitch-dn](https://github.com/Glitch-dn)  
**Software created for educational purposes**
