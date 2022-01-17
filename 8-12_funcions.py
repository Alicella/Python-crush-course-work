def sandwiches_order(*types):
    print("\nThe following sandwiches are ordered:")
    for type in types:
        print("- "+ type)

sandwiches_order('chicken', 'fish')
sandwiches_order('beef', 'tuna', 'vega')