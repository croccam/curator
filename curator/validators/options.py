from voluptuous import *
from ..defaults import option_defaults

## Methods for building the schema
def action_specific(action):
    options = {
        'alias' : [
            option_defaults.name(action),
            option_defaults.warn_if_no_indices(),
            option_defaults.extra_settings(),
        ],
        'allocation' : [
            option_defaults.key(),
            option_defaults.value(),
            option_defaults.allocation_type(),
            option_defaults.wait_for_completion(action),
            option_defaults.wait_interval(action),
            option_defaults.max_wait(action),
        ],
        'close' : [ option_defaults.delete_aliases() ],
        'cluster_routing' : [
            option_defaults.routing_type(),
            option_defaults.cluster_routing_setting(),
            option_defaults.cluster_routing_value(),
            option_defaults.wait_for_completion(action),
            option_defaults.wait_interval(action),
            option_defaults.max_wait(action),
        ],
        'create_index' : [
            option_defaults.name(action),
            option_defaults.extra_settings(),
        ],
        'delete_indices' : [],
        'delete_snapshots' : [
            option_defaults.repository(),
            option_defaults.retry_interval(),
            option_defaults.retry_count(),
        ],
        'forcemerge' : [
            option_defaults.delay(),
            option_defaults.max_num_segments(),
        ],
        'open' : [],
        'reindex' : [
            option_defaults.request_body(),
            option_defaults.refresh(),
            option_defaults.requests_per_second(),
            option_defaults.slices(),
            option_defaults.timeout(action),
            option_defaults.wait_for_active_shards(action),
            option_defaults.wait_for_completion(action),
            option_defaults.wait_interval(action),
            option_defaults.max_wait(action),
            option_defaults.remote_certificate(),
            option_defaults.remote_client_cert(),
            option_defaults.remote_client_key(),
            option_defaults.remote_aws_key(),
            option_defaults.remote_aws_secret_key(),
            option_defaults.remote_aws_region(),
            option_defaults.remote_filters(),
            option_defaults.remote_url_prefix(),
            option_defaults.remote_ssl_no_validate(),
        ],
        'replicas' : [
            option_defaults.count(),
            option_defaults.wait_for_completion(action),
            option_defaults.wait_interval(action),
            option_defaults.max_wait(action),
        ],
        'rollover' : [
            option_defaults.name(action),
            option_defaults.new_index(),
            option_defaults.conditions(),
            option_defaults.extra_settings(),
            option_defaults.wait_for_active_shards(action),
        ],
        'restore' : [
            option_defaults.repository(),
            option_defaults.name(action),
            option_defaults.indices(),
            option_defaults.ignore_unavailable(),
            option_defaults.include_aliases(),
            option_defaults.include_global_state(action),
            option_defaults.partial(),
            option_defaults.rename_pattern(),
            option_defaults.rename_replacement(),
            option_defaults.extra_settings(),
            option_defaults.wait_for_completion(action),
            option_defaults.wait_interval(action),
            option_defaults.max_wait(action),
            option_defaults.skip_repo_fs_check(),
        ],
        'snapshot' : [
            option_defaults.repository(),
            option_defaults.name(action),
            option_defaults.ignore_unavailable(),
            option_defaults.include_global_state(action),
            option_defaults.partial(),
            option_defaults.wait_for_completion(action),
            option_defaults.wait_interval(action),
            option_defaults.max_wait(action),
            option_defaults.skip_repo_fs_check(),
        ],
    }
    return options[action]

def get_schema(action):
    # Appending the options dictionary seems to be the best way, since the
    # "Required" and "Optional" elements are hashes themselves.
    options = {}
    defaults = [
        option_defaults.continue_if_exception(),
        option_defaults.disable_action(),
        option_defaults.ignore_empty_list(),
        option_defaults.timeout_override(action),
    ]
    for each in defaults:
        options.update(each)
    for each in action_specific(action):
        options.update(each)
    return Schema(options)
