eneration'])
    # Sort by highest sum likelihood
    df = df.sort_values('likelihood', ascending=False, ignore_index=True)
    return df.loc[0].text

print(getSummary(prompt1))
