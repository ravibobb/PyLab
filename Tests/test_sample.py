import SnowflakeLib.SfConnect as sf

def test_rowcount():
    qry = "select distinct Top 5 Country from netflix_titles"
    count = sf.get_rowcount(qry)
    assert count == 5
