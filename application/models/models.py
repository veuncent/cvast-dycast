import logging

from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry


DeclarativeBase = declarative_base()



# Helper functions

def create_tables(engine):
    logging.info("Creating tables...")
    DeclarativeBase.metadata.create_all(engine)



# Entities

class Case(DeclarativeBase):
    """SQLAlchemy Case model"""
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True)
    report_date = Column(DateTime)
    location = Column(Geometry(geometry_type='POINT', srid='3857'))

class DistributionMargin(DeclarativeBase):
    """SQLAlchemy Distribution Margins model (Monte Carlo)"""
    __tablename__ = "distribution_margins"

    number_of_birds = Column(Integer, primary_key=True, index=True)
    close_pairs = Column(Integer, primary_key=True, index=True)
    probability = Column(Float)
    cumulative_probability = Column(Float)
    close_space = Column(Integer, primary_key=True, index=True)
    close_time = Column(Integer, primary_key=True, index=True)

class TmpDailyCaseSelection(DeclarativeBase):
    """SQLAlchemy Daily Case Selection model"""
    __tablename__ = "tmp_daily_case_selection"

    case_id = Column(Integer, primary_key=True)
    report_date = Column(DateTime)
    location = Column(Geometry(geometry_type='POINT', srid='3857'))

class TmpClusterPerPointSelection(DeclarativeBase):
    """SQLAlchemy Cluster Per Point Selection model"""
    __tablename__ = "tmp_cluster_per_point_selection"    

    case_id = Column(Integer, primary_key=True)
    report_date = Column(DateTime)
    location = Column(Geometry(geometry_type='POINT', srid='3857'))

class Risk(DeclarativeBase):
    """SQLAlchemy Risk model"""
    __tablename__ = "risk"

    risk_date = Column(DateTime, primary_key=True)
    lat = Column(Float, primary_key=True)
    long = Column(Float, primary_key=True)
    num_birds = Column(Integer)
    close_pairs = Column(Integer)
    close_space = Column(Integer)
    close_time = Column(Integer)
    nmcm = Column(Float)