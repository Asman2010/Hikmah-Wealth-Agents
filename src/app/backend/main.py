#!/usr/bin/env python
from backend.crew import HikmahWealthAgentsCrew


def run(ticker: str):
    inputs = {
        'company': ticker
    }
    HikmahWealthAgentsCrew(query=ticker).crew().kickoff(inputs=inputs)
    
