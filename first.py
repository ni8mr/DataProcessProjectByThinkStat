"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import survey


def mean(t):
    """Computes the mean of a sequence of numbers.

    Args:
        t: sequence of numbers

    Returns:
        float
    """
    return float(sum(t)) / len(t)


def partition_records(table):
    """Divides records into two lists: first babies and others.

    Only live births are included

    Args:
        table: pregnancy Table
    """
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()

    for p in table.records:
        # skip non-live births
        if p.outcome != 1:
            continue

        if p.birthord == 1:
            firsts.add_record(p)
        else:
            others.add_record(p)

    return firsts, others


def process(table):
    """Runs analysis on the given table.

    Args:
        table: table object
    """
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = mean(table.lengths)


def make_tables(data_dir='.'):
    """Reads survey data and returns tables for first babies and others."""
    table = survey.Pregnancies()
    table.read_records(data_dir)

    firsts, others = partition_records(table)

    return table, firsts, others


def process_tables(*tables):
    """Processes a list of tables

    Args:
        tables: gathered argument tuple of Tuples
    """
    for table in tables:
        process(table)


def summarize(data_dir):
    """Prints summary statistics for first babies and others.

    Returns:
        tuple of Tables
    """
    table, firsts, others = make_tables(data_dir)
    process_tables(firsts, others)

    print 'Number of first babies', firsts.n
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, others.mu

    print 'Mean gestation in weeks:'
    print 'First babies', mu1
    print 'Others', mu2

    print 'Difference in days', (mu1 - mu2) * 7.0


def main(name, data_dir='.'):
    summarize(data_dir)


if __name__ == '__main__':
    import sys

    main(*sys.argv)
