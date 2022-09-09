# WAX Release Notes

## General

WAX software version 2.0 is a port of WAX-specific patches to EOSIO
2.0 software by Block.One.

The upgrade procedure from WAX 1.8.4 to 2.0 is similar to upgrading
EOSIO from 1.8 to 2.0. The release notes of EOSIO apply to WAX
software as well. All WASM virtual machine options available in EOSIO
are also supported in WAX, and recommendations on their use are the
same as for respective releases of EOSIO software.

Unlike 1.8, the server version string is controlled by
`CMakeLists.txt` and is no longer derived from Git tags.

In order to keep most compatibility with upstream software, the
proposed versioning schema will add `waxNN` to VERSION_PATCH in
`CMakeLists.txt`.


## Release `v2.0.5wax01`

EOSIO 2.0.4 was merged with WAX 1.8.4, with necessary
modifications. Later on, EOSIO 2.0.5 was merged in.


The following files were taken from vanilla EOSIO without
modifications, because WAX changes were not necessary:

```
libraries/testing/include/eosio/testing/tester.hpp
libraries/testing/tester.cpp
```

`scripts/eosio_build.sh`: `-r` option in wax-1.8.4 is setting
PUBLIC_ROOT_KEY, but it's not used in release binaries. Skipping in
wax-2.0.


`unittests/eosio_system_tester.hpp` line 415: set buyram sum to "0.5
WAX".

Testing scripts were adjusted and bugfixed, so that full automated
testing can succeed on WAX.


## Release `v2.0.9wax01`

EOSIO 2.0.9 merged

## Release `v2.0.10wax01`

EOSIO 2.0.10 merged

## Release `v2.0.11wax01`

EOSIO 2.0.11 merged

## Release `v2.0.12wax01`

EOSIO 2.0.12 merged

## Release `v2.0.13wax01`

EOSIO 2.0.13 merged

## Release `v2.0.13wax03`

EOSIO branch release/2.0.x merged up to commit 173261f4 (Big ship deltas - 2.0)

## Release `v2.0.13wax04`

Merged https://github.com/eosnetworkfoundation/mandel/tree/release/2.0.x
up to commit 3e7cbe13f04c2e1df687b09695418a4c7dd9d1b8
Merge pull request #99 from eosnetworkfoundation/config-sub-decay-2.0
Configurable subjective account decay time - 2.0

New configuration option: "subjective-account-decay-time-minutes"
Recommended value is 60 wherever subjective billing is enabled.

## Release `v2.0.14wax01`

Merged with v2.0.14 from https://github.com/eosnetworkfoundation/mandel/tree/release/2.0.x
Apply 3-strike rule for complete block production

## Release `v2.0.14wax02`

Merged with https://github.com/AntelopeIO/leap/tree/sub-bill-uint32-2.0
uint32_t for microseconds of subjective billing only allows for 1.2hrs
before wrapping. Use int64_t instead which matches type used for objective billing.

