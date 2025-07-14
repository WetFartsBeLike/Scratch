import scratchattach as sa

session = sa.login("CuteCatUltra", "Dacat5769")

server = sa.init_cloud_server(
    "127.0.0.1", 8080,
    thread=True,
    length_limit=None, allow_non_numeric=True,
    whitelisted_projects=None, allow_nonscratch_names=True, blocked_ips=[]
    sync_players=True
    log_var_sets=true
)
