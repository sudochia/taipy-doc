if __name__ == "__main__":
    import taipy as tp
    import my_config

    tp.Core().run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    sequence = scenario.sales_sequence
    sequence.submit()
