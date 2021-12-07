"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation=None, name=None, diameter=None, hazardous=False):
        """Create a new `NearEarthObject`.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        if not designation:
            self.designation = '' 
        if not isinstance(designation, str):
            try:
                self.designation = str(designation)
            except:
                raise TypeError(f"designation must be a str")
        self.designation = designation   

        # if not name:
        #     self.name = '' 
        if not isinstance(name, str):
            try:
                self.name = str(name)
            except:
                raise TypeError(f"name must be a str")
        self.name = name  

        if not diameter:
            self.diameter = float('nan')
        if not isinstance(diameter, float):
            try:
                diameter = float(diameter)
            except Exception as e:
                print(diameter)
        self.diameter = diameter  

         
        if not isinstance(hazardous, bool):
            try:
                hazardous = bool(hazardous[0])
            except:
                print(hazardous)
        self.hazardous = hazardous 

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        fullname = f"{self.designation} + {self.name}"
        return fullname

    def __str__(self):
        """Return `str(self)`."""
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and [is/is not] potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, calendar_date, distance, velocity):
        
        if not distance:
            self.distance = float('nan')
        if not isinstance(distance, float):
            try:
                distance = float(distance[0])
            except:
                print(distance)
                
        self.distance = distance  

        if not velocity:
            self.velocity = float('nan')
        if not isinstance(velocity, float):
            try:
                velocity = float(velocity[0])
            except:
                raise TypeError("velocity must be float")
        self.velocity = velocity  


        if not designation:
            self._designation = '' 
        if not isinstance(designation, str):
            try:
                self._designation = str(designation)
            except:
                raise TypeError(f"designation must be a str")
        self._designation = designation   

        calendar_date = str(calendar_date[0])
        self.time = cd_to_datetime(calendar_date)
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"At {self.time_str}, '{self.neo.fullname}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"

# tests
# python3 -q
# from models import NearEarthObject, CloseApproach
# neo = NearEarthObject(designation="looks chill", name="rik",diameter=99)
# ca = CloseApproach(neo, '2020-Dec-31 12:00', 201212, 60)
