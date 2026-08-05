timestamp 2026-05-07 03:45:44
#lastapply no-merge

#.. checked up to PR #35239 / gui#936 / knots#303

checkout v28.2
@28.x-syslibs
# BUILD BUGS:
	TODO: #32299
	5872 subdir_incl_compat						b7dd5799936
	# For Qt6: g837
	#29.xTODO# If needed? 30997 hebasto/240928-qt6 and/or g861 whitslack/qt6
	# Only needed with Qt6: -     qt_scope_bringToFront_workaround-28
		# Related to gui#914 hebasto-g/251121-wayland
	32437 fanquake/extend_asan_sse4
	Triage: 32484 fanquake/28_suppress_unterm_string_init
	Triage: Part of? 32551 hebasto/250518-crypto-macros
	Triage: Needs review: 33550 ryanofsky/pr/winstream
	Triage: Needs review: 33569 l0rinc/l0rinc/throw-by-value
	Triage: Needs review: 33570 l0rinc/l0rinc/environ-mingw
	Triage: Partial: 33779 hebasto/251104-force-iwyu-kernel
	Triage: 34093 fix_freebsd15_netlink_warn				last=c1361fc42dd vasild/fix_nlmsg_ok_compilation_fbsd15
	(CHECK-LAST)	last=490cd874a40 origin-pull/34680/head^  # 29.x backport
	k246  fix_boost1.73compat-29
		# https://github.com/bitcoin/bitcoin/issues/34101
	34462 fix_bsd_batchprio-26
	Triage: Needs review: 34591 hebasto/260214-cmake-macos-cross
	Triage: Review: 34953 deadmanoz/fix/gcc-asan-sha256-sse4-only
	Triage: 35068 ryanofsky/pr/depfind
	-     compatfix_boost_1.91-28
		# Similar to #35175 (but without the regression)
			NOTE: (which has a 28.x backport in #35214)
# SYSLIBS: (and old build bugs)
	2241  sys_leveldb-28+knots					91af8d0c4ea	last=dd10cff7dd0 sys_leveldb
		# WIP c8e8c03997a dbwrapper: Return util::Result for SanityCheck (only needed for libbitcoinkernel?)
		# Related: #32447
		# If https://github.com/bitcoin-core/leveldb-subtree/pull/52 is merged, this should possibly be adapted
	5416  sys_libsecp256k1-28					3d441102525	last=5acc3a1c534 sys_libsecp256k1
	# TODO: sys_crc32c ??
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	#29.xTODO# sys_libminisketch
	13789 bugfix_asm_pragmas-26					22df203e4cd	last=4d9aff4d0b2 asm_bypass_cxxflags
	(CHECK-LAST)	last=6878dd8f1ab origin-pull-k/309/head
		TODO: + knots#309
	15155 test_external_bcli					7d6366b5659
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# Meh? 34390 fanquake/tar_override_get_prev
	# If needed: 35080 maflcko/2604-test-time-factor
	n/a   (delete_release_notes_fragments)
@28.x-knotsfixes
# TESTS:
	# If needed: -     ci_knots-26							e2099d64846
	-     lint_relaxer-28+knots					efeece9f031
	-     nowarn_unreachable-code-28			ad6a12d7bbc	last=1f0489e215f nowarn_unreachable-code
	-     nowarn_unused-function				45a2e5951ce
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	# If needed: -     ci_i686mp_clang15						955f1eeed99
	31408 qafix_framework_pr31408-27			8d7611a7eca
	# Needs review: k209 mstampfer/test-feature-block-bad-version-log
	# Triage: Only if native Windows CI: 32219 -
		# NOTE: incomplete backport at c939d74b244
	TRIAGE: 33639 maflcko/2510-ci-rework-cache-providers
	33990 qa_rpc_startingheight-28							last=52f96cc235d theStack/202512-test-announced_starting_height
	Triage: 34185 brunoerg/2025-12-test-pruning-wout-wallet
	# Only if native Windows CI? 34285 hebasto/260114-windows-pyzmq
	# FreeBSD: 34346 w0xlt/freebsd_high_port_range-again
	# Only if native Windows CI? 34418 hodlinator/2026/01/31409_fix
	n/a   fix_dbcrash_timeout_pr34589part-0.16
		# Part of #34589
	34622 qafix_debuglog_races_pr34622-29.3+k
		# NOTE: Excludes timeout relaxation
	# If needed: 34690 maflcko/2602-test-zmq
		# NOTE: 30.x backport in #34689
	Triage: If needed: 34728 maflcko/2603-test-wallet-assume-sync
	Triage: Needed in 2026 April: 34815 willcl-ark/bump-cirruslabs-actions
		# See also: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
	# Needed in 2027 October (Python 3.16): 34820 maflcko/2603-test-windows-revert
	# If needed: 34914 Sjors/2026/03/deep-sign (CI macOS codesigning)
	35161 qa_merkle_mutated_rv-0.19							last=f2dbc6a5fd5 l0rinc/l0rinc/doc-merkle-root-mutated
		# Test only
	35164 qa_p2sh_sigop_counting-23							last=f1884695736 musaHaruna/test/p2sh-sigop-counting
	# Needs concept & review: 35216 hebasto/260505-illumos-bind
	35218 qafix_fuzz_p2sh_offset_pr35218-25
# FIXES:
	33433 qafix_rpc_bind_nonloopback_unavail
	18818 guix_reltar_autogen_distclean			5bd6cb2eb0a	last=b5a164d9155 fix_gitian_src_202004
	(CHECK-LAST)	last=3efb06b858b rm_minisketch-29+syslibs
		#29.xTODO# Check GenerateBuildInfo.cmake ?
	18902 fix_gitdir_again						506a39d8934
	(CHECK-LAST)	last=903fc971ed6 fix_gitdir_foreign
	(CHECK-LAST)	last=69066e2af56 relsrc_embed_tagname-29+knots
		# NOTE: based directly on #18818
	18427 2020mingwthrd-mini-23					da1e5f9ffae	last=63768965f1c 2020mingwthrd-mini
	18490 bugfix_symcheck_pe_case				d2d3b434b08
	Maybe disabled by default? 32604 Crypt-iQ/log_ratelimiting_05192025
		# +#33011 ? + #33211 ?
		# Formerly: 21603 dergoegge:log_ratelimiting
		# NOTE: Formerly Needs review: 19995 practicalswift/mitigate-log-disk-filling-attacks
		# OR Needs review (and set default OFF?): 21706  # log: Mitigate disk filling attacks by globally rate limiting LogPrintf(…)
		# 29.x backport in #33225
	14968 http_bind_error-26					def0d7f8f83	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	(CHECK-LAST)	last=57becdf59e5 http_bind_error
	-     http_bind_error+extra-26				d0f65e2f2e4	last=fc1d58d4d03 http_bind_error+extra
		# NOTE: libevent-copied code up to date as of 2023-11-22 cfb2b89a1d0642abd6389913e237f49c662502e4
	 9524  rpc_pruneblkchain0					85dc1e1fc32	last=88883ae13d
	10731 log_more_uacomment-28					cbfa6e5b9be	last=b9d2634b81d log_more_uacomment
	29614 bufferedfile_fclose					4be2187282d
	14485 fadvise-28+knots						efcc7b7a087	last=549717f0a8a fadvise-29+knots
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					cfdde513b64
	-     fix_rpc_arg_multiname					3b0c1f0add6
	-     bugfix_rpc_getbalance_hacky			ccf3424296e
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted -OR- 27539 Empact/2023-04-minimum-file-descriptor-18911
	# Needs review: 16050 promag:2019-05-importmulti-update
	18194 bugfix_gui_edit_sendaddr-mini			e9d0a3182b0	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				12d357c6255	last=3f9cc0cd736 Saibato/wallet_351
		# NOTE: modified to use std::set and diff-minimise
			# NOTE: fixed to include <set> instead of <algorithm>
		# NOTE: added default "blocks" dir to exclusions
	# Needs review: 19434 promag:2020-06-remote-disconnect OR 27245 fjahr/202303-pr19434 OR 27909
	# Needs review: g59   hebasto-g/200814-rpc
	# Needs concept/review/triage? 19876 -  # wallet: Fix wallet loading race during node start
	# Needs review: 19880 -  # fix CTxMemPool::TrimToSize to put only confirmed coins in pvNoSpendsRemaining
	# Needs work, not important: 20383 practicalswift/signed-integer-malformed-mempool-dat-and-rpc
		#TODO: diff-minimise, review
	# Needs review: minimise g129 -  # qt: Fix Shortcut Ambiguities, Clean up text
	g152  gui_notify_setup_bg					f81eeca008a
	-     bugfix_gui_drop_abc_confusing_hack	85e32c93b2b
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	g236  gui_init_walleterror_cont				d40c1220043
	-     rpc_addconnection_mainnet				72ac99f48a5
	32343 subproc_closefds-28					fd30be38f53	last=4f79dfd99f6 subproc_closefds
		# Was #30756
		# Replaces #22417 (Boost::Process variant)
		FIXME: address #33063
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				159d9c36b05
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs work: 32964 w0xlt/r_26573
		# Was #26573 darosior/taproot_over_dont_under_estimate
		# Was #23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
		# NOTE: If we're sending to someone else who is paying the tx fee, it actually makes sense?
	g506  qt_qrcode_sizefixes					36c41fed21b
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	24066 -  # contrib/init: (OpenRC) use -daemonwait to wait for startup completion
	-     openrc_from_gentoo
		# Other OpenRC updates from Gentoo:
		# - PIDDIR in /run instead of /var/run
		# - LOGDIR var added
		# - RPC cookie group-readable
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				7dc92f9cc9f
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-28+knots			bea0c626a1a	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	g595  qt_handle_autostart_errors-0.15		3da9f0c4b0b	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	-   gui_psbt_error_msgbox-28				5a1384386db	last=a3eec5c3f70 gui_psbt_error_msgbox
		# WAS: g599  ts_20220515-partial-25				5191aa16ac2	last=d9411324066 ts_20220515
			# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
			#TsTODO# Update with other commit (unit translations) when translations supported again
	29868 hww_windows-28						301886f3d0e	last=86c7c65e2fe hebasto/240414-win-subprocess
	(CHECK-LAST)	last=0d687e37252 hww_windows-29
		TODO: add #32358 & #32567
		# NOTE: Retained `ENABLE_EXTERNAL_SIGNER` cmake option
		# Replaces: -     hww_windows-27						e1f9c1bbde8
			# Reverts #29489 & #28967
	# Check on #25561 (nonsense signed int overflow in leveldb?)
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	g633  -										2b6dec6757f	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	g662  qt_fix_txview_202209					0e9150347ec
		# Includes gui#368
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	# TODO: Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	# TODO: Sane fix for #24049
	g677 fix_qt_peers_na						db82f05cfd3
	# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs work: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-28+knots	f182f096cf2	last=a6f567590b7
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	#29.xTODO# CAUTION: #27307 was merged, but "this appears to possibly show a higher balance than the user actually has for sure??" - investigate
	# Alternative to: 27434 pinheadmz/chaintips-invalid
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#28.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     qafix_assert_debug_log_create			8d840e79471
	-     acceptstalefeeestimates_mainnet_opt	04db65df5ea
		# Currently (28.1) needs qafix_assert_debug_log_create
	# Needs review: 27684 hebasto/230516-punish OR ???
	#28.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 -										387a5cf295c	last=bfc2bb6a270  # forbid_nohelp-0.19
	(CHECK-LAST)	last=916c1b855ec forbid_nohelp-29
	27815 -										838b286095e	last=244e6c8db81  # cli_forbid_multihelper-22
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	# Needs review: 27912 -  # net: run disconnect in I2P thread
	# Needs work: 27973 maflcko/2306-byte-span-
	28029 fix_zmq_errhandling_202307-mini-26	24565dab864	last=ba28af94bd5 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		52de30f4845
	# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs review: 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	# Needs review: 28248 jonatack/2023-08-network-diversity
	28345 fix_bytespersigop_checks-mini			8e36b819288	last=6f627727739 fix_bytespersigop_checks
		#29.xTODO# NOTE: Excludes removal of buggy wrapper for diff-minimisation; needs checking manually (to ensure wrapper doesn't get used even in final/complete merge of all PRs) when assembly done; known issues: stash 172d7d7a9
		# Related bug in #18479
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	28564 fix_conf_fuzzbin_main					86c5ef3785b
	28616 assumeutxo_unconfirmed_ux_Sjors-28	f7e50a7e3f3	last=3e281590c7d Sjors/2023/10/assume-unconfirmed
	-     assumeutxo_unconfirmed_ux-28			46c7684bc14	last=7a832effaa6 assumeutxo_unconfirmed_ux-29
	-     qt_recomm_confirms-0.9				3a77d04cbd5
		# NOTE: Un-hardcoding 6 already taken care of in assumeutxo_unconfirmed_ux above (956546a1f2f)
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: 28724 achow101/cleanup-accidental-watchonly-mkeys
	# Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	-     fix_keep_notmy_cookie					16aacf2a6f8
		# Originally part of #28784, but regressed in d95dde9441f...7cb9367157e
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	28944 rpc_sendall_anti_fee_sniping-28		25117369373	last=b11d00d54ed ishaanam/sendall_anti_fee_sniping
		# + #33118
	Review: 35019 HouseOfHufflepuff/rpc/uniform-locktime-anti-fee-sniping
	-     rpc_walletcfpsbt_antifeesniping-28+k
	(CHECK-LAST)	last=113ba106273 Sjors/2025/07/locktime
		# Includes tests from #32892
	29141 fix_rpcauth_blank-24					3ad996f41bb	last=51588287fb5 fix_rpcauth_blank
	# Needs work: 29147 guix_attachable_sigs					ad4fe4b83a4
		# GPG discourages clearsign signatures!
		#29.xTODO# but windows has lots of problems with existing style...
		#29.xTODO# but deviating from Core signing may reduce participants?
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29175 -										5f08e7fee5b	last=be8ae64b82e  # rpc: validate fee estimation mode case insensitive (fix_rpc_estmode_unset_case-24)
	# Needs work: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	29307 AutoFile_error_check-28				17291246d08	last=dba78353868 vasild/AutoFile_error_check
	(CHECK-LAST)	last=72d5b71c196 AutoFile_error_check-29
	# Needs work: g792 -  # Correct tooltip wording for watch-only wallets
	29480 -										91fbf239a90	last=88468a8afcd  # log_rand_during_init-0.20
		# Needs careful backport (basically rewritten)
	# Nothing to fix? 29589 -  # tests: fix OP_1NEGATE handling in CScriptOp
	29640 fix_tiebreak_on_disk-26							last=177d07f6591 sr-gi/202403-block-tiebreak
	(CHECK-LAST)	last=d97d221376c origin-pull/34521/head
		# IMPORTANT: Adds a UB bugfix
		# left off doc change (4caa38600e6)
		TODO: + #34521 if ready (better UB fix? addresses assumeutxo?)
	#28.xTODO# Needs review: 29652 ryanofsky/pr/noloc
	#28.xTODO# Needs review: 29664 mzumsande/202403_near_tip_stalling
	29678 fix_init_lowdisk_warning_reqd-28		8c4f8f40807	last=b1117e5a716 fix_init_lowdisk_warning_reqd
	(CHECK-LAST)	last=58ceddd389e fix_init_lowdisk_warning_reqd-29
		# Excluded dev doc update
	# Needs review: 29680 -  # wallet: fix unrelated parent conflict doesn't cause child tx to be marked as conflict
	# Needs review: 29770 fjahr/2024-03-check-undo-index
		# +#34991 ? (31.x backport in #35231)
	# Needs review: 29796 fanquake/depends_0g_debug_flags
	-     fix_rpc_warnings_all-28				6fb830e0d2d
	# Needs review/concept: 29877 0xB10C/2024-04-tracing-cast-duration-to-µs
	g815  fix_qt_privacy_before_open-23			20bc0e347cd	last=0dc337f73d0
		# Rewrote myself due to overcomplication and race bug in PR
	# Not worth it? 29963 hebasto/240425-guess-cc
	# Needs review: 30065 sr-gi/2024-05-fdcount
	#28.xTODO# Needs review: 30079 ismaelsadeeq/05-2023-ignore-transactions-with-parents
		# Was: 25380 darosior/fee_estimator_disable_cpfp
	-     jonatack/2024-05-fix-cjdns-detection-in-AddNode	0a3e577e9e8	last=be4541abe59 jonatack/2024-05-fix-cjdns-detection-in-AddNode  # fix_cjdns_addnode_detect2-27+knots
	# Needs review: 30155 mzumsande/202405_replay_blocks OR 33442 l0rinc/l0rinc/interrupt-rolling-forward
	# Needs review & diff-minimising: 30207 mzumsande/202405_invalid_chains
	30221 fix_wallet_bestblock-29.3
		# aka knots#290
		# +#32281 +#32580 +#32345
		# Excluded 30a94b1ab9ae850d55cb9eb606a06890437bc75e (test removal) for diff-minimising
	# Needs work: g823 -  # wallet: Improve error log color in the console
	-     detect_clang_bug96267-28				6da92446b43	last=159eef5ccb2 detect_clang_bug96267
	# Needs review: 30359 -  # Correct Error Code in OP_IF/OP_NOTIF Empty Stack Check
	# Needs review: 30410 mzumsande/202407_getblock_error
	# Needs review: 30469 fjahr/2024-07-csi-overflow-2
		# Was: 26426 fjahr/202210-coinstatsindex-overflow
	30479 mzumsande/202407_fix_resetfailure
	30508 fix_depends_zmq_cmake_pc-28			155737973b5
	# Needs review: 30529 ryanofsky/pr/listset
	# If needed? 30489 theuni/depends-zmq-patch
	30666 mzumsande/202404_invalidblock
	# Needs (concept?) review? 30678 fjahr/2024-08-backup-best
	# Needs work: 30679 tdb3/handle_invalid_rpcbind_port
	# Needs review? 30684 furszy/2024_init_negated_args_err
	30794 SignatureHash_int32_hashtype			ef2f78b9214	last=bc52cda1f3c
		# +31365 TheCharlatan/consensus_sighash_int_type
	# Needs review: 30844 furszy/2024_rpc_wallet_sffo_duplicates
	# Needs review: 30866 achow101/multipath-spkm-fuzz-crash
	30909 fix_GVP_assumeutxo_pr30909-28			046057b0df0	last=9d2d9f7ce29 fjahr/2024-09-au-guess
		# NOTE: Just the bugfix for now
	30929 log_enforce_newline-28				56c2250df4a	last=fa2b7d8d6b3 maflcko/2409-log-nl
		# NOTE: Minimal, only to ensure new code backports correctly
	# Needs review: 30972 BrandonOdiwuor/wallet-listreceivedby-fix
		# was: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	30979 upd_asmap_uri-28						7f327e7df06
	31064 init_coins_cache_pr31064-25			878cbd9c54c
	# WIP: 31096 txpkg_sz_1-28										last=d4fcca53231 instagibbs/2024-10-submitpackage-singleton
	31097 scripterr_prefer_consensus-28			ef80edf7c01
	31124 disable_rand_perfmon-0.20				4e75910f284
	31212 improve_args_pr31212-28				771789a3001
		# +#31433
		# Excluded due to newer Python requirement: 1ab3d515af9 refactor test: Cleaner combine_logs.py logic
	g836  fix_qt_opts_proxy_ipv6-24				88243053a15
	31275 fix_rpc_example_quoting_pr31275-24	ad6c4570514	last=49ffbc6077d
	# Needs work? (adds overhead) 31298 -  # rpc: combinerawtransaction now rejects unmergeable transactions
	# OR: Needs work: 33361 -  # Fix #25980: Validate transactions in combinerawtransaction
	31343 qa_dummy_proxy-21						0247e6fe0b8
	31646 qafix_inet_access_pr31646-28			bb9302e344a	last=2ed161c5ce6 vasild/test_avoid_internet_traffic
	# Needs work: 31349 vasild:test_log_internet_traffic
	# Maybe not relevant? 31346 Sjors/2024/11/init_m_tip_block
	31374 fix_wallet_migrate_pr31374-27			8b315fea6e6	last=cdd207c0e48 furszy/2024_migration_watch-only_crash_fix
	31376 mining_curtime_avoid_timewarp-28		32bb226fa2c	last=733fa0b0a14 darosior/2411_miner_never_timewarp
	# Needs work: 31378 furszy/2024_wallet_migration_multisig_crash
	31383 qafix_ibd_stalling_pr31383-28			751244b972c
	# Needs work: 31384 ismaelsadeeq/11-2024-fix-duplicate-coinbase-reservation-bug
		# NOTE: Not so high a priority when blocks are already too big
	31391 custom_iso8601datetime-28+knots		7fbcebdee49
	# Needs review: 31404 furszy/2024_descriptors_infer_multisig
	# Needs careful review: 31405 mzumsande/202411_stricter_invalidblock_handling
		#+32843
	31416 docfix_rpc_send_inputsobj-23			4df3333de0f	last=fad83e759a4 maflcko/2412-doc-rpc
	# Needs review: 31439 mzumsande/202412_reindex_interrupt
	# Needs review/correctness per branch: Diff-minimise: 31449 -  # coins,refactor: Reduce getblockstats RPC UTXO overhead estimation
	31451 fix_wallet_migrate_wo_bdb-27			f187eddc341	last=589ed1a8eaf furszy/2024_migration_cleanup_after_error
		# First half of commit silently assumes wallet is unloaded before migration (from #31248 in 29.x)
	Unclear if applicable to Knots: 31453 macos_exfat_warning-28+knots			25f0359c100	last=df1ba101419 willcl-ark/macos-exfat
	(CHECK-LAST)	last=bd2e2e1cc2c macos_exfat_warning-29+knots
		# Dropped doc change (links to Core github)
		# Added warning before leaving GUI firstrun screen
		TODO: Knots gets rid of likely-buggy macOS-specific AllocateFileRange in fix_preallocate, so it's unclear if this is an issue for us
	# Needs review: 31495 achow101/migrate-corner-case-scripts
	31514 -  # wallet: allow lable for external descriptor & disallow label for ranged descriptors
	31529 upd_glibc_mte_strncmp-28				eedd55a773d	last=b8710201fbd fanquake/glibc_2_31_latest
	# Complex Triage: 31556 mzumsande/202412_assumeutxo_wallet
	# Needs review & backport work: 31590 achow101/fix-constpubkey-xonly-getprivkey
		# Attempted backport in 74c7aa7133b
	# Not strictly a bug? 31603 brunoerg/2025-01-descriptor-pk
	# Needs work? 31610 l0rinc/l0rinc/gettransaction-rpc-doc
	# Needs work: 31615 -  # Ensure assumevalid is always used during reindex
	31617 qafix_db_tests_wo_bdb-24				6a03f82b3fb
	g850  qt_psbt_sighash_default-28			ff9c8155fd4	last=3e97ff9c5ea achow101-g/gui-psbt-sighash-default
	31622 achow101/psbt-sighashes
NM	31623 tracing_MIN_macro_rename				f7ec451c999
	# Approach NACK? 31629 mzumsande/202501_rescan_bestblock
	#29.xTODO# Triage: 28521 hodlinator/2024/12/disconnecting
	31655 fix_sha3_ub_pr31655-21				19ca155a548
		# Just the fix
	31661 fix_deps_libevent_build_type-28		a8e00aa12d3
	31671 fix_leveldb_ptrarith_pr31671-28		0fc02402ef0
		# Just the fix
	31674 lock_blocksdir-28						ff1b8720f3e
		# Diff-minimised
	Triage: 31629 mzumsande/202501_rescan_bestblock
	31727 darosior/2501_miniscript_nonfatal
		+ 32255
	# Needs review? 31734 -  # miniscript: account for all StringType variants in Miniscriptdescriptor::ToString()
	# Needs review? 31767 -  # Ensure -debug=0/none behaves consistently with -nodebug
	# Needs review? 31774 -  # crypto: Use secure_allocator for AES256_ctx
	# Needs work & importance: 31775 -  # rpc: collect transaction fees on generateblock
	# Needs review: 31785 Sjors/2025/02/create_new_block
		# CAUTION: This may depend on other PRs
	# Needs review: 31794 furszy/2025_wallet_abandon_coinbase_during_startup
	# Needs review: 31807 theuni/fix-dupe-kernel-symbols
	# 31912 workaround_buggy_rndrrs-28			36e11bb93cc	last=2498dd8dbd5  # random: Check GetRNDRRS is supported in InitHardwareRand to avoid infinite loop
		# Held back 585aba6eec8..2498dd8dbd5 (2x diff for basically the same thing)
	32248 laanwj/2025-04-remove-arm64-rndr
	# Needs review? 31835 -  # validation: set BLOCK_FAILED_CHILD correctly
	# Needs work: 31888 midnightmagic/fix-linearize-gjpyn
	# Needs review: 31929 hodlinator/2025/02/stop_http_robust
	31958 docfix_rpc_wallet_cf_psbt-24			ee76cf26ae7	last=0ad066c85a4  # rpc: add cli examples, update docs
	31979 tor_backoff_max-26					056c95b3ff8	last=f708498293c  # torcontrol: Limit reconnect timeout to max seconds and log delay in whole seconds
	Triage: 32049 -  # contrib: Fix gen-bitcoin-conf.sh
	# Needs review: 32051 jonatack/2025-03-addnode-p2p
	32073 netinactive_dont_downgrade-26
	# Needs concept & review: 32123 -  # wallet: make coinbase that will mature on the next block available for selection
	# Needs review: 32143 -  # Fix 11-year-old mis-categorized error code in OP_IF evaluation
	32176 tor_rnd_stream_isolation-28
		# Omitted renaming variable
	# Needs review: 32180 mzumsande/202403_ibd_lastcommonblock
	32185 fix_dbwrapper_batch_header_size-26
		# Only the fix, without the bumped LevelDB version dep
	# Needs review: 32186 -  # descriptor: handle listdescriptors(private=true) for taproot descriptors having partial keys
NM	32187 zmq_devirtual_destructor-0.12
	# Needs review: 32199 maflcko/2504-time
	g864  fix_qt_shutdowncrash_g864-24						last=c6f4b0d7960 furszy/2025_gui_fix_crash_numBlocksChanged
	# ----- IN SEQUENCE, NEEDS BACKPORT REVIEW IN #35226 -----
	Needs backport review: 32602  # fuzz: Add target for coins database
		# Includes first commit of #32279 for #32313
	Needs backport review: 32313  # coins: fix cachedCoinsUsage accounting in CCoinsViewCache
	Needs backport review: 34207  # coins/refactor: enforce GetCoin() returns only unspent coins
	Needs backport review: 34164  # validation: add reusable coins view for ConnectBlock
	Needs backport review: 33512  # coins: use dirty entry count for flush warnings and disk space checks
		# Adds a tag to the CoinsViewCacheCursor constructor to avoid silent conflicts
		# Diff-minimises entire sequence
	# ----- END SEQUENCE -----
	32333 doc_rpc_pruneblockchain_top-21					last=135a0f0aa71
	32342 -  # Fix missing error check in set_clo_on_exec for FD_CLOEXEC handling
	32344 fix_wallet_nonranged_pr32344-22					last=97d383af6d5
	32351 qafix_nonrecurs_FindChallenges-28
	32355 fix_block_full_enough
	# Needs review: 32367 hebasto/250428-enable-lang
	-     fix_fs_error_utf8-23
		# Alternative to core#32383 hebasto/250429-fs-error
	32414 fix_reidxcs_periodic-25							last=c1e554d3e58 andrewtoth/reindex-flush
		# Fix only
		# TODO: consider performance refactor?
	# Simplified rewrite of? 32528 maflcko/2505-1
		# Was (unreleased) #31135 jonatack/2024-10-verification-progress or #31177 polespinasa/verificationProgress
	# Needs concept: 32530 darosior/2505_limit_mempool_32bit
		# NOTE: 29.x backport in #32810
		# NOTE: release note in #32819
	Needs review: 32539 pinheadmz/rpcallowip-rfc4193
	32553 achow101/wallet-log-minversion
	# Needs work: 32577 hebasto/250521-subprocess-split
		# FIXME: Ensure this gets resolved before #32566 is merged
	# Needs review: 32606 davidgumberg/5-23-25-ignore-unsolicited
	# Needs review and simplification? 32636 davidgumberg/5-27-2025-create-refactor
		# + fix from #34490
	Triage: 32646 instagibbs/2025-05-fillblock-mutated
		# 29.x backport in #33344
	32682 fix_wallet_fillpsbt_nothrow-28
		# Diff-minimised only
	# Needs review: 32685 -  # wallet: Allow read-only database access for info and dump commands
	32708 docfix_listdescriptors_nonimported-23
	32736 fix_listwalletdir_err-23
	# Needs review: 32757 -  # net: Fix Discover() not running when using -bind=0.0.0.0:port
		# Was #31492 (not in any release)
		# Or #33935
	# Needs review: 32773 hebasto/250618-mkdir
	# Needs concept & review: 32788 achow101/desc-allow-H
		# Check for this impacting other Knots merges
	32826 p2p_badports_dbm_rdp_vnc-23
	# depends-only, needs work: 32837 fanquake/fix_libevent_mingw_w64_13
	Triage: 32845 pablomartin4btc/rpc-fix-unloadwallet-when-no-wallet-name-nor-context
	# Needs concept & review: 32869 instagibbs/2025-07-invalid-cb-stall
	32878 HowHsu/rewind
	32943 fix_deps_cmake_no_exportpkg-28
	Triage/Minimal: 33001 maflcko:2507-test-actually-fail-on-failure
		28.x backport in #33076
	Triage: Needs review: 33014 b-l-u-e/fix-32849-descriptorprocesspsbt-internal-bug
	# Needs review: 33072 b-l-u-e/p2p-fix-nscore-overflow-24049
	33105 cve2025_46598_pt1-29.1
	32473 cve2025_46598_pt2-29.1
	33050 cve2025_46598_pt3-29.1
	Review: 33119 -  # rpc: Fix 'getdescriptoractivity' RPCHelpMan, add test to verify fix
	# Needs concept/work: 33127 Ataraxia009/launch-crash-failure
	33133 docfix_getpeerinfo_ping_secs-25					last=1252eeb997d 0xB10C/2025-08-fix-getpeerinfo-ping-docs
	# Needs review: 33135 Sjors/2025/08/older-safety
	# Needs review: 33164 hebasto/250809-fallback-fallocate
		# NOT SUFFICIENT WITHOUT:
	33228 fix_preallocate
		# Includes less-than-ideal workaround for https://github.com/bitcoin/bitcoin/issues/33128#issuecomment-3203396013
	Review: 33212 mzumsande/202508_index_nocommit
		# NOTE: 29.x backport in #33251
	33215 fix_debuglog_refs_hardcoded-28+knots
		# Includes gui#884 hebasto-g/250819-debuglog
	Needs review? 33223 murchandamus/2025-08-tiebreak-SRD
	# Needs work: 33231 w0xlt/mulitple_binds
	# Needs review: 33268 achow101/zero-value-from-me
		# 30.x backport in #33356
	# Needs review: 33296 Crypt-iQ/cmpctblock_assume_fix_09032025
		# 29.x backport in #33344
	# Needs review: 33297 -  # cmake: Inherit WERROR setting for secp256k1 build
	33310 wrkarnd_gcc_systemtap_ice
	33340 hebasto/250908-fix-csv
		# 28.x backport in #33415
	# Needs review: 33358 -  # contrib: fix for macOS deployment build failing on Qt translations even though it is optional.
	# Needs review: 33360 -  # rpc: Add validation for invalid taproot signatures in analyzepsbt
	33395 mzumsande/202509_whitelist_onion
		# 28.x backport in #33415
	# Needs concept: 33427 john-moffett/rpc-submitpackage-reportall
	# Needs review: 33430 john-moffett/rpc-addpeeraddress-error
	Triage: g886  wrkrnd_qt_textedit_oom-0.14
	# Needs review: 33443 l0rinc/l0rinc/rate-limit-rolling-forward
	# Needs review: 33444 -  # rpc: Fix dumptxoutset rollback with competing forks
	# OR (preferable): 33477 fjahr/202509-better-rollback
	# Needs work? g895  benthecarman-g/fix-dark-mode
	33464 net_timers_for_inbound_inv-29
	Triage: 33475 ismaelsadeeq/09-2025-miner-infinite-loop-fix
		# 30.x backport in #33473
	33484 docfix_rpc_finalizepsbt_pr33484-0.18
	33494 urlupd_depends_qrencode-28						last=93a70a42d30 hebasto/250929-qrencode
		# NOTE: Held back 9dbfce7fc84...93a70a42d30 (which drops package name from download filename) and addressed cache filename issue another way
	# Needs review: 33498 -  # p2p: Mitigate GETADDR fingerprinting by setting address timestamps to a fixed value
	33504 instagibbs/2025-09-truc-reorg-fix
		28.x backport in #33535
	33563 fanquake/fix_qt_urls
	# IPC-specific: 33566 Sjors/2025/10/wait-empty-mempool
		# 30.x backport in #33609
	33580 achow101/depends-fallback-name
	# Needs review: 33604 -  # p2p: Allow block downloads from peers without snapshot block after assumeutxo validation
	# n/a until a test needs 29.1-29.99: 33612 Crypt-iQ/log_ratelimit_functional_backport_10132025
		# 30.x backport in #33609
	# Needs review: 33616 instagibbs/2025-10-bypass_checkephemeral
	# Needs review: 33646 -  # log: check fclose() results and report safely in logging.cpp
	# Needs review: 33663 -  # addrman, net: Filter during address selection via AddrPolicy to avoid underfill
		# Or #34162 fjahr/2025-12-33663-alt
	33698 fix_qa_rpctimeout_pr33698-27
	# Needs review: 33699 0xB10C/2025-10-addr-token-bucket-start-5
	Triage: n/a   restore_dnsseed_luke-jr-29.3
		# Reverts #33723
	# Needs review: 33727 -  # zmq: Log bind error at Error level, abort startup on init error
	g901 fix_qt_rpchistoryfilter_pr_g901-28
	# Needs concept: g905 -  # Increase tooltip wrap threshold from 80 to 100 characters
	33813 Ataraxia009/rpc-bind-warning
	Triage: Needs review: 33854 -  # fix assumevalid is ignored during reindex
	Triage: 33865 hebasto/251112-plugin-path
	Triage: 33952 fanquake/close_out_29977
	33956 fix_p2pv2_useafterfree_pr33956-26
	Triage: 33960 maflcko/2511-log
	# Triage: IPC-specific: Needs review: 33965 Sjors/2025/11/ipc-reserve
	33993 doc_stopatheight_imprecise-21
	34028 fix_seenlocal_max-26								last=33103d5c4fe
		# Held back pointless duplication 3fc5948e1fe...33103d5c4fe
	-     fix_feeest_read_rare_overflow-29
		# Alternative to: 34109 maflcko/2512-fix-u64
	-     pcp_dont_spam_unauth-29
	(CHECK-LAST)	last=af5c2fcf144 origin-pull/34117/head
		# TODO: Consider replacement with #34549
		# Inspired by the first commit on #34117
	# Needs concept/review: 34117-commit-2  net: fix CJDNS address discovery when -externalip is set
	Triage: Needs review: Partial: 34143 hebasto/251223-boost-layout
	Needs review: 34146 0xB10C/2025-12-separate-self-announcement
		+ #34297 (p2p: add validation checks for initial self-announcement)
		+ #34717 ?
	# ----- WALLET DELETION BUGFIXES -----
	Review: 34156 furszy/2025_wallet_migration_jinglewreck
		Ensure /wallet.dat doesn't rm /
		Ensure user-made files in wallet dir survive
		test when wallet is loaded (or not) when migratewallet called
		test if unloadwallet settles wallet file
		30.x backport in #34209
	Review: 34215 achow101/createfromdump-deletion
		28.x backport in #34223
	Review: 34226 davidgumberg/2026-01-07-relative-path-migration-failure
		30.x backport in #34229
	32273 -  # wallet: Fix relative path backup during migration
		# DO NOT MERGE WITHOUT FIXING WALLET DELETION BUG
		# NOTE: Held back "wallet: migration: Make backup in walletdir" behaviour change
	34370 fix_34222_backport
		NOTE: 28.x backport in #34620
	34372 qa_wallet_migration_tests_202601-29.3
		# NOTE: Invisible dependencies on #32273 and #34370
	Triage: 34176 handle_wallet_dir_nonwritable-29.3				last=08925d5ee75 furszy/2025_wallet_check_db_permissions
		# NOTE: temporarily restored `descriptors=True` in tests until bdb is updated to pass
	Triage: -     handle_wallet_dir_nonwritable_bdb-29.3
	Triage: 31423 wallet_migrate_watchonly_only-29.3
		# NOTE: Includes parts of #32984 and #34156
	Triage: 34193 furszy/2026_wallet_safer_MigrateToSQLite
	# Needs review: 34198 furszy/2026_wallet_migration_ancient_wallets
	k242 fix_bdb_edge_cases_202601-29
	k269 wlt_migrfail_cleanup_lognonempty-29.3
	TODO: consider knots#249 review comments
	# ----- END WALLET DELETION BUGFIXES -----
	34161 fix_distance_ub_pr34161-26						last=477c5504e05 l0rinc/l0rinc/pool-allocator-ub
	34227 hebasto/260108-guix-osslsigncode
		28.x backport in #34270
	# IPC-specific: Triage: 34184 Sjors:2025/12/cool-down
	# Needs review/work: 34213 brunoerg/2026-01-net-anchors-networkactive
	34224 fix_init_int_ec-27
	34235 fix_miniminer_feeassert_pr34235-26
	34252 doc_bips_add433-28
	Triage: Needs review: g915 -  # Defer transaction signing until user clicks Send
	# Redundant with gui#677 (which fixes more): g920  -  # Set peer version and subversion to N/A when not available or detecting
	# Redundant with gui#815 (which fixes more): Needs review: g922  -  # gui: fix transactions disable problem
	Triage: 34293 fix_vermsg_missing_comma-29+knots					last=ffd09f8a0d0 fix_vermsg_missing_comma
	34272 fix_psbt_bounds_assert_pr34272-25
	Triage: Needs followup work? 34281 maflcko/2601-build-fix-remove
		30.x backport in #34283
		+ #34413 (see also issue #34414)
		+ #34468 ?
	34282 qafix_win_log_skips_pr34282-24
	Triage: 34305 fanquake/fix_space_warning_log
		Consider CeilDiv from #34436
	Triage: 34328 l0rinc/l0rinc/uptime-monotonic
		+ #34437
	Triage: Needs review: 34348 -  # lib: call RandFailure() if RDRAND fails
	Triage: Needs review? And/or minimal fix instead? 34349 maflcko/2601-sp-popen-less
	Triage: Needs review? 34358 mzumsande/202601_importprunedfund_bug
	34369 maflcko/2601-test-scale-close-timeout
	Triage: Needs review: 34371 -  # wallet: allow importprunedfunds for spending transactions
	Triage: Needs review: 34379 rkrux/gethdkeys
	Triage: Needs review: 34381 brunoerg/2026-01-scriptnum
	Needs review: 34393 -  # rpc: Fix off-by-one error in getblockchaininfo help
	Triage: 34417 maflcko/2601-log-warn-sensitive
	g924  fix_qt_restor_empty_walletname_msg-24
	Triage: Needs work: 34451 w0xlt/i_34263
		# +#34908 ?
	# Windows-only, doesn't affect us? 34454 avoid_winnt_delete_keyword_conflict-28
	Triage/needs review: 34456 -  # p2p: assign separate network keys to outbound onion connections
	Triage: Needs review: 34458 sedited/logips_self_discover
	Triage: Needs review: 34467 -  # net: don't perform network activity when networkactive=0
		OR: 34486 willcl-ark/respect-networkactive
	34470 leveldb_wrkrnd_uninit_debugsize-0.8				last=fad7d86d8d1 maflcko/2602-ci-leveldb-ub
	Needs review: 34480 danielabrozzoni/issue/26527-dont-backtime-nlocktime-unconf
	Triage: Needs review (and AI removal?): 34530 -  # wallet: guard against negative bump fee discount from mempool race
	Triage: Needs review/concept: 34538 willcl-ark/onlynet-advertisments
	34561 docfix_rpcwallet_send_eg_pr34561-23				last=50cf6838e6a
	Needs review: 34582 maflcko/2602-int-arg
	34597 fix_SetStdinEcho_ub-0.20
	34603 fix_win_IsSymlink-29.3							last=677297e8522
	Needs review? 34614 maflcko/2602-ci-space
	g929  qt_plurals_prg929-21								last=746d8cddc19 hebasto-g/260217-translation-plurals
	Triage: Needs review: 34628 ajtowns/202602-mempool-invtosend
	34642 wallet_validqueue_drainforunload-29.3+knots
		# NOTE: Subtly depends on #30221 (and the PRs bundled with it)
	Triage: 34655 l0rinc/l0rinc/coins_view_fuzzer_cleanup
	Triage: IPC mining: 34661 ryanofsky/pr/waitmine
	# Doc fix: 34671 maflcko/2602-doc-guix-less
		# NOTE: 29.x backport in #34680
	Needs review: 34678 chriszeng1010/fix-accept-unknown-sockaddr
	34702 docfix_getblock_txfee_condition-22				last=f580cc7e9f2
	Needs review: 34743 willcl-ark/protect-manual-evictions
	34767 fix_qt_intro_chain_except
	Triage: 34787 fanquake/ci_test_macos_codesigning
		NOTE: 31.x backport in #34800
		NOTE: 30.x backport in #34805
	Triage: Needs concept & review: 34812 w0xlt/fix-33471-cjdns-externalip
	n/a   fix_typos_from_pr33152-29.3
	Triage: 34870 furszy/2026_feebumper_crash_fix
	Needs work: 34872 w0xlt/wallet-mixed-input-history-only
	34888 furszy/2026_wallet_total_amount_bad_comparison
	Review: 34893 w0xlt/psbt-proprietary-merge-fix
	Review: 34897 mzumsande/202603_index_sync_dont_commit_ahead
	Needs review: 34903 HouseOfHufflepuff/wallet-importdescriptors-validate-before-rescan
	Needs review: 34916 Sjors/2026/03/manpages-locale
	Needs review: 34931 furszy/2026_utxo_deser_error_divergence OR 34132?
	Needs work: 34937 Sjors/2026/03/file-descriptor-limit
	Review: g934 sbddesign-g/fix-151-issues-with-new-create-wallet-dialogue
	34959 bdbro_enforce_levels_sizes-28						last=b2de59d486d achow101/bdbro-cycle-detection
		# OR: 34946 instagibbs/2026-03-infinite_migrate
	Triage: Needs review: 34962 cprkrn/test-feebumper-enormous-cluster
	# Needs review: IPC only: 34978 enirox001/04-26-ipc-maxconnections
	# Needs review: IPC only: 35037 enirox001/04-26-ipcbind-max-connections-draft
	34988 fix_init_fiasco_pr34988-28
	Needs review: 34993 davidgumberg/2026-04-02-notifycan
	Needs review: 34997 danielabrozzoni/getaddr_feeler
	Needs review: 35003 furszy/2026_abc_io_exception
	Triage: Review: 35017 instagibbs/2026-04-remove_all_consensusscript
	Triage: Needs careful review: 35026 javierpmateos/fix-bip68-stale-lockpoints-clean
	Triage: 35168 fix_exclude_pruned_from_unlinked-29
		# Includes test framework addition of create_empty_fork from #32587
	Triage: 35070 stratospher/2026_04_m_blocks_unlinked_ub
	Needs review: 35071 pinheadmz/reindex-continue
	# Needs review: 35137 GerardoTaboada/wallet/document-maxconf-default
	# Triage: Needs review: 35143 thomasbuilds/fix-btck-handle-self-move-assign
	Needs review: 35145 ViniciusCestarii/verifydb-cleanup
	-     fix_torcontrol_maxlinelen-29+knots
		# Includes new tests (only) from #34158
	35087 torcontrol_linelimit-29+knots						last=9fe5896a446 davidgumberg/2026-04-14-torcontrol-linelimit
	Needs review: 35092 -  # wallet: bound descriptor update work after high-index detection
	Needs review: 35100 nervana21/20260416_locktime
	Needs review: 35115 tony-ku/wallet-34599-abandon-confirmed-descendant
	OR: 34599 Luquitasjeffrey/issue34599
	35116 socks5_redact_authinfo_log-28
	35117 i2p_redact_privkey_in_log-22						last=cd2833e7436 takeshikurosawaa/i2p-session-create-redaction
	Needs review? 35166 asafmod/harden-prevector-change-capacity
	Needs review? 35173 l0rinc/l0rinc/thread-name-truncation
	Triage: Needs review: Or fix-only? 35177 AgusR7/test/getblockstats-gen-miniwallet
	Needs review: 35185 shuv-amp/fix-importdesc-timestamp-abort
	Needs review: 35191 ArtSabintsev/codex/fix-txdb-cursor-malformed-key
	Needs review & UPnP: 35193 vasild/avoid_internet_traffic_from_init_test
	Needs review: 35208 l0rinc/l0rinc/headerssync-future-mtp-cap
	35209 fix_precomptxdata_lifetime_CVE_2024_52911-27
	# Needs review: 35217 -  # psbt: fix PSBTInput::Merge ignoring sighash_type field
	35227 fix_bdbro_check_lastpage_pr35227-28				last=e2b0984f995 l0rinc/l0rinc/check-bdb-last-page-lsn
	Needs review? 35233 l0rinc/l0rinc/external-signer-skip-canceled-duplicates
	35384 fix_settings_writeerror_handling-27
	-     fix_qt_sync_pct_truncate-28						last=a3dac13371c origin-pull-g/935/head
		# Rewrote from gui#935 to avoid floating point rounding at any stage
	-     fix_rpccookieperms_early-28+knots		dec38cfcc7b	last=e49dfac3241 fix_rpccookieperms_early
	-     qt_intro_nojumpy						4ee79cc6ff2
	-     restore_guix_ppc64le-28				72fda2e9327
	-     qt_dialogs_less_modal					2822662e04d
	Triage: -     fix_qt_startup_unknown_unit
	Triage: -     fix_qt_psbtops_filename_amount
	k126  fix_qt_progressbar_fittext
	k150  fix_rpc_mixed_params_edgecases
		# Held back (4d24d60836f) support for positional options + named params (breaks tests)
	Needs work: k182 proxy input validation fixes
	# Needs work: k228 1440000bytes/fix-corruptwallet-crash
	-     qt_nowalletpage_alerts-23
	-     fix_alertnotify_winquoting
	-     torcontrol_avoid_bindany_connect
	-     fix_tor_common_bind-29.2
		# Core duplicate: #34892
	Needs review: k254 privkeyio/cmake-hardening-module
	Needs review: k237 privkeyio/159-build-checks
	k244  fix_qt_amtfield_infinityevent
	-     fix_win_exclopen-29.3
	k255  wlt_nonlegacy_change_if_no_leg_spkman
	# n/a to Knots: -     depends_libevent_ignore_git_desc
		# Only affects libevent builds when the bitcoin tag has 5 components
	Needs work: k263  privkeyio/fix-vsize-sigops-datacarrier
	k266  extsigner_sanitychk_fingerprint-26				last=acc78e798fa privkeyio/fix-external-signer-fingerprint-validation
	k277  fix_qt_ban_expiry_update-28						last=87fca974185 Bortlesboat/fix-ban-table-refresh
	Needs review: k298 param_bounds_checks_202604
	k301 qt_always_show_alerts-27							last=3437824d39b privkeyio/fix-warnings-no-wallet-tabs
	k303 rm_dnsseed_pt
	k329 privkeyio/fix-gen-bitcoin-conf-datadir				last=4f5c53851fa
	k336 qt_locale_datetime_prk336-29+k						last=2f53648f1a2 privkeyio/fix-gui-datetime-locale
		# Second commit included later in softwareexpiry
	k339 privkeyio/fix-pie-c-link-flags						last=66dc2de6c25
	k344 -													last=2b54c093cf1 privkeyio/fix-rpcconsole-wallet-selection-consistency
	k352  MaximeMRF/fix/tor-datadir-spaces
	#28.xTODO# "Knots feature request: system notification for a txn should show the net wallet balance delta assuming the txn confirms, not whatever it does now that gives me a heart attack every time I use a large-ish UTXO lol" -Jason (currently only the first send of a sendmany is shown) https://github.com/bitcoin-core/gui/issues/853
	# TODO: prunenotify to run a command after each prune (eg, for fstrim or such)
	
	# FIXME: How to unify listtransactions and GUI tx list? GUI has net changes, while RPC just has positive fees
	# FIXME: watchonly indicator is confusing.
		# See * c2436937613 Bugfix: GUI/Wallet: Decompose watch-only flag for each logical transaction
			# Holding back in hopes of potential RPC+GUI unification
		# But not sure it's worth breaking RPC?
	# FIXME: workaround #26025 / https://github.com/llvm/llvm-project/issues/57587 ?
	# FIXME: https://twitter.com/tchjntr/status/1788332365887995925
		# weird bitcoin.conf results in:
		#	ASSERT failure in QList<T>::operator[]: "index out of range", file /bitcoin/depends/x86_64-w64-mingw32/include/QtCore/qlist.h, line 575
	# TODO: ensure that rejecting a tx also rejects dependents in the orphan pool
	#28.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@28.x-knots-lts-deps
	-     upd_qt5-28							1774fb76e0e	last= upd_qt5-29.2
		FIXME: Check #30774 for updated patch?
		# Opensource released: https://lists.qt-project.org/pipermail/announce/2024-November/000526.html
		TODO: Qt 5.15.17 + CVE-2025-4211
		TODO: 5.15.19 Opensource released: https://lists.qt-project.org/pipermail/announce/2026-May/000626.html
	#28.xTODO# FIXME -     depends_qt5kde
	k345 privkeyio/depends-libevent-2.1.13					last=0515b85e4f3
	# Needs review & relevance: 29991 fanquake/sqlite_3_45_3
	30301 theuni/miniupnp-228-bump
	(CHECK-LAST)	last= origin-pull-k/196/head
		TODO: Include knots#196
	TODO: bump to 2.3.3 in restore_upnp-29.2+knots
	# Needs review: 32655 fanquake/sqlite_3_50_0
	# Needs review: 32665 fanquake/boost_shrink
	Triage: -     fix_secp256k1_bugs-29
		# bitcoin-core/secp256k1#1731,1749,1821 (diff-minimised and fix-only)
	Triage: Multiprocess-only: 34825 fanquake/capnp_1_4_0
	Triage: Multiprocess-only: 34952 ryanofsky/pr/subtree-9
		+ #34977 ?
@28.x-knots
# PERFORMANCE:
	n/a   rm_minisketch-28+k					723ceffb7b7	last=3efb06b858b rm_minisketch-29+syslibs
	33915 qa_getprevrel_retrydownload-28
	# Needs review: 24158 JeremyRubin/epoch-mempool-reorg-updates
	# Needs review: 24589 -  # sha512.cpp improvements
	# Probably a bad idea: 24712 -  # wallet: reduce coin selection iterations
	# Knots doesn't support MSVC builds: 24773 Enable AVX2 implementation of SHA256 for MSVC builds
	# Needs work: 24901 -  # mempool: reduce lookups, insertions to cache in UpdateForDescendants
	# Needs review: 24926 -  # mempool: use mapNextTx.lower_bound in removeRecursive
	# Needs review: 25236 -  # wallet: use vector instead of list for transactions
	# Needs review & diff-minimising: 25297 -  # wallet: speedup transactions sync, rescan and load not flushing to db constantly
	# Needs review: 32740 danielabrozzoni/upforgrabs/25968
		# Was (not in Knots): 25968 sipa/202208_headerssync_optimize
	# Unclear benefit: 26375 zmq_optimise_duplread-27+k			3f9e56d77af	last=7b631dc9b19 andrewtoth/no-read-zmq
		# Several improvements in Knots branch
		# Post-#26415(merged), it's unclear if this is an improvement or potentially a performance loss: we either readback raw (from OS cache), or serialize CBlock
	# Needs review: 26486 sipa/202211_batchnotfound
	# Opt-in & needs review: 26951 pstratem/2023-01-23-gcsfilter
	# Needs review: 26966 furszy/2022_parallelize_blockfilter_index_2
	# Needs review: 27006 furszy/2022_reduce_cs_main_scope_blockindex_nfile
	# Needs concept/review: 27050 -  # p2p, validation: Don't download witnesses for assumed-valid blocks when running in prune mode
	# Needs review: 27427 -  # validation: Replace MinBIP9WarningHeight with MinBIP9WarningStartTime
	# Needs review? Part of? 28226 martinus:2023-08-more-CBufferedFile
	-     dbcache_1TB-0.13						2ed340330f1	last= (upstream)
		# Inspired by #28358 Sjors/2023/08/double-your-coins---cache (needs work)
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										5b3fb3eeb0f	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 txrelayrate_14txps-26					88f7b4153a1 last=b81f37031c8
		# TODO: Make configurable? Or is that even sane?
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Needs more careful review: 29436 addrman_select_networks-26						last=7edb07ca800 brunoerg/2024-02-addrman-select-networks
	# Needs review: 29473 -  # optimization: Speed up Base58 encoding by 400% by 64-bit preliminary byte packing
	# Needs review: 29491 fjahr/2024-02-batch-validation-updated
	# Needs review: 29578 brunoerg/2024-03-addrman-getaddr
	29602 -  # refactor: Optimize IsSpace function for common non-whitespace characters
	# TODO: Revert #29815 ? (ie, use OS provided optimised timingsafe_bcmp)
	30059 dbfilesize_param-26					add2386fdc7	last=1c2c840aff9 dbfilesize_param
	(CHECK-LAST)	last=ecc7ba40daa dbfilesize_param-29+knots
	(CHECK-LAST)	last=ecc7ba40daa dbfilesize_param-29.1
	-     dbfilesize_64-26						6d097aed47f	last= dbfilesize_64-29.1+knots
	(CHECK-LAST)	last= dbfilesize_64-29+knots
		# Was: #30039 (128 MiB originally, settled on 32 MiB)
		# Note: Upstream PR uses std::max with LevelDB's current default, in case LevelDB changes theirs to larger
	# Needs review: 30093 -  # refactor: reserve memory allocation for transaction outputs
	# Needs review: 30317 -  # WIP Simplify SipHash
	# Needs review: 30325 -  # optimization: Switch CTxMemPool::CalculateDescendants from set to vector to reduce transaction hash calculations
	# Needs review: 30370 fjahr/2024-07-pr28945
		# Was (never in Knots) #28945
	# Needs review? 30442 paplorinc/paplorinc/siphash
	# Needs review: 30610 sipa/202408_force_sync OR 33680 l0rinc/l0rinc/force-sync
	30611 andrewtoth/write-chainstate-every-hour
		TODO: #32414 has new tests on top of #30611
		TODO: Make interval configurable
	30675 -										b5e9df40d6d	last=03d49d0f25a  # http: set TCP_NODELAY when creating HTTP server
	# Needs diff-minimise? 30884 sipa/202409_reduce_ftell_xor
		# check if 30927 has anything important
	# Needs Knots review & diff-minimise: 30987 davidgumberg/zero_after_free_allocator_change
	# Needs review: 31132 andrewtoth/threaded-inputs
	31144 l0rinc/l0rinc/optimize-xor
	31179 opti_rpc_uv_reserve-25				fd9df84d86b	last=5d82d92aff7
	31364 opti_no_copy_pr31364-28				3614ce28149
	# Needs review: 31490 l0rinc/l0rinc/undo
	31551 l0rinc/l0rinc/bulk-block-read-write
	31645 opti_dbbatchsize_64-0.15				ef2cf259a11	last=868413340f8 l0rinc/l0rinc/utxo-dump-batching
		# TODO: Test even higher or incrementing-as-we-flush
	# Needs review: 31682 l0rinc/l0rinc/optimize-CheckBlock-input-duplicate-check
	# Needs Review? 31714 mzumsande/202501_simpler_segwit_check
	# Needs reivew: 31868 l0rinc/lorinc/block-serialization-optimizations
	# Needs review: 31875 l0rinc/l0rinc/sorted-BatchWrite
	# Needs work: 32023 -  # wallet: removed duplicate call to GetDescriptorScriptPubKeyMan
		# +#32475
	# Needs review: 32128 -  # Draft: CCoinMap Experiments
	# Needs review: 32150 murchandamus/2025-03-rewrite-BnB
	32279 l0rinc/l0rinc/prevector-size
	32487 l0rinc/l0rinc/optimize-readblock-hash-check
	-     netproc_check_blockhash
	# Needs review: 32497 opti_merkle_reserves-21							last=39b6c139bd6 l0rinc/l0rinc/pre‑reserve-merkle-leaves-to-max
	# Needs careful review: 32532 l0rinc/l0rinc/short-circuit-known-script-types
	# Needs review: 32645 theStack/202505-fs-use_ftruncate_on_openbsd
		# NOTE: ftruncate does not guarantee allocation normally? and we don't want to truncate!
	# Needs work: 32692 -  # TODO: Dynamic scriptcheck thread count
	# Needs review: 32730 furszy/2025_net_avoid_traversing_block_twice
	# Needs review: 32791 -  # checkqueue: implement a new scriptcheck worker pool with atomic variables
	32827 opti_removeForBlock_empty-28						last=54f9cb85c4b l0rinc/l0rinc/empty-mempool-IBD
	Review: 32885 pstratem/2025-07-05-lockless-isibd
	# Needs review: 33031 achow101/lasthardened-cache-migratewallet
	33217 fanquake/drop_xinerama
		# Broken backport to 29.x in #33238
	# Needs review: 33253 ajtowns/202508-cache-friendly-compactblock
	#28.xTODO# 33264 kevkevinpal/reduceScopeOfGetBlockTemplateLock
	# Needs work? 33299 mzumsande/2025_wallet_log_less
	33304 fanquake/strip_qt_bins
	# Needs review: 33306 fjahr/2025-09-csi-compaction
	# Conflicts with #18014? Needs review: 33325 Raimo33/siphash-write-chunked
	# Needs review: 33328 -  # Mapping for Lockedpool
	33332 fjahr/2025-09-trivial-copy
	Review: 33334 Raimo33/index-work-comparator-branchless
	33410 opti_coinstats_nocopy_pr33410-26		30ada41e121	last=85d058dc537  # coinstats: avoid unnecessary Coin copy in ApplyHash
		# Real last=5a56203f4e4 (branch messed up by author)
	# Needs review? 33602 l0rinc/l0rinc/BatchWrite-lookup-optimization
	# Needs review: 33637 l0rinc/l0rinc/block_index_comparators
	# Needs review: 33645 Raimo33/optimize-tx-policy-verification
	Review: Partial: 33738 l0rinc/l0rinc/debug-log-serialization
	# Needs review: 33757 l0rinc/l0rinc/solutions-vector-optional
	# Needs concept (even if merged) & review: 33817 l0rinc/l0rinc/bip30-bloom-filter-removal
	# Needs careful review: 34004 -  # Implementation of SwiftSync
	Triage: 34025 ajtowns/202512-netsplit-opt
	# Needs review: 34054 sedited/txdownloadman_ibd_check
	# Needs review: 34083 theuni/chacha20-vectorized-initial
	Needs 28.x review: 34253 lockless_isibd-26+knots							last=557b41a38cc l0rinc/l0rinc/cache-ibd-status
		# NOTE: diff-minimised, and did not backport refactor commits
		# NOTE: various libbitcoinkernel changes needed, if libbitcoinkernel features (#30595 in particular) are backported
	# Needs review: 34400 -  # wallet: parallel fast rescan (approx 5x speed up with 16 threads)
		# + #34667 ? +#34907 ?
	# Needs review: 34405 -  # wallet: skip APS when no partial spend exists
	# Needs review: 34424 -  # [RFC] CChain Concurrency Improvement (Base + Tail Architecture)
	# Needs review & worth-it evaluation: 34483 maflcko/2602-span-reader
	# Needs review: 34489 furszy/2026_index_batch_processing
	Triage: 34612 fanquake/unused_historgram
	Needs review? 34613 -  # replace manual byte copies
	Just removes a Guix dep: 34627 fanquake/replace_sponge
		+ #34944 ?
	# ----- DBCACHE DEFAULT/WARNING -----
	33333 dbcache_too_high_warning-29.3+knots
		# + #33435
	34692 dbcache_1GiB-29.3+knots							last=4ae9a10ada9 andrewtoth/bump_dbcache
		# Excluded doc update & release notes
	35097 byte_units_64bit_GiB-29.3+knots
		# Partial; + #34435 (partial)
		# Fixed missing header
	34641 dbcache_dynamic-29.3+knots
		# + #34106 copyright notice + misc fixups
		# Omitted refactors, doc changes & release notes
		# NOTE: last= removed because upstream branch destroyed
	Needs review: 35200 l0rinc/l0rinc/smooth-dbcache-warnings
	# After working mempressure: k279  privkeyio/feature-autosize-dbcache
	# TODO: cgroup-awareness as a default limit? (see also #34762)
	# ----- END OF DBCACHE DEFAULT/WARNING -----
	Needs review: 34656 alexanderwiederin/blockmap-chain-concurrency
	Needs review: 34794 w0xlt/rest-cache-control-headers
	Needs concept & review: 34932 w0xlt/cmpctblock-shortid-collision-recovery
	Needs review: 35041 brunoerg/2026-04-descriptor
	35128 l0rinc/l0rinc/dbwrapper-key-spanreader
	35156 l0rinc/l0rinc/ScopedDataStreamUsage
	35195 cache_outpoint_sethash-27							last=16e77fdf132 l0rinc/l0rinc/noexcept-false
	35197 lld_icf_safe-28									last=09de5363d36 fanquake/lld_icf_safe
	Needs review: 35215 l0rinc/l0rinc/siphash-jumbo
	35825 privkeyio/net-addconnection-count-guard-core		last=ca7c1456f56
	Needs review: k278  privkeyio/feature-runtime-scriptcheck-calibration
	k287  privkeyio/uncap-scriptcheck-threads				last=f23f08cb01f
	# TODO: dumptxoutset doesn't return until chain is rolled back forward
# SOFTFORK:
	# TODO: 31989 CheckTemplateVerify
		# Was #21702 (never in Knots)
	# TODO: 28550 jamesob/2023-09-covtools-softfork
	# TODO: 29050 stevenroose/txhash
	# TODO: 29198 reardencode/lnhance
	# TODO: 29221 -  # Implement 64 bit arithmetic op codes in the Script interpreter
	# TODO: 29247 -  # Reenable OP_CAT
	# TODO: 29269 -  # Add OP_INTERNALKEY for Tapscript
	# TODO: 29270 -  # Implement OP_CHECKSIGFROMSTACK(VERIFY)
	# TODO: 29280 -  # Implement OP_CHECKTEMPLATEVERIFY
	# TODO: https://github.com/jamesob/bitcoin/tree/2025-06-ctv-csfs CTV+CSFS combined
	# TODO? 30018 -  # Implement BIP 118 validation (SIGHASH_ANYPREVOUT)
	# TODO? 32080 -  # OP_CHECKCONTRACTVERIFY
	# TODO? 32247 jamesob/2025-04-csfs
	# Needs community support: 33163 -  # BIP360 quantum
	# Triage: 34140 roconnor-blockstream/simplicity
	# TODO? k222  -  # taproot/script limits; default unknown-witness off; BIP8 stub
	# NOTE: knots#238 (RDTS) moved to end of branch assembly!
	# Needs review & consensus: 34419 Sjors/2026/01/bip-coinbase-fields
	# Needs review & consensus: 34826 sashabeton/p2skh
# FUNCTIONALITY:
	-     rm_kernel_lib							84b7c6adf43
		# TODO: Support libbitcoinkernel (see 9da0bc3eba7 history for incomplete attempt)
			# When restoring libbitcoinkernel support, adjust libbitcoinconsensus reverts to make it interact with --with-libs (see 7ad32d39d76)
	# Broken: 24448 guix_linux_i686_compat				e8a7da94969	last=c76ac9d57f2 guix_linux_i686
		# test2: export of symbol _IO_stdin_used not allowed!
		# test2: libutil.so.1 is not in ALLOWED_LIBRARIES!
		#'test2: failed EXPORTED_SYMBOLS LIBRARY_DEPENDENCIES
	# not ready: 8889 overlay_theme-0.13								last=f8a28dc
	# needs UI improvements!? 7949 jonasschnelli/2016/04/rpc_signals
	# TODO: Just forgetaddress from #8488
	#8549 jmcorgan/zmq_mempool
			# check if issue mentioned in 7753 still exists
	# not ready yet: 9483 SPV
	# wait for SPV: 9502	# [Qt] Add option to pause/resume block downloads
	# not ready?? 9722 GUI: Display warning when attempting address reuse (wallet format changes!)
	# not ready: 9745 [RPC] Getting confirmations command
	# needs updating: 10200 sdaftuar:2017-04-dont-mine-recent-tx
	# Needs fixing/review: 17303 maflcko:1910-p2pNoRemovedTxs
	# Needs review: 17332 sdaftuar:2019-10-no-checkpoints-cleanedup
	# Needs concept + ???: 15341 promag/2019-01-bumpfee-changeaddress
	# TODO: MAYBE OPTIONAL 12578 promag:2018-03-fee-transaction-record
	# TODO: 12705 kallewoof/importmulti-wif-support
	# TODO ? 12792 w/ renamed param
	18479 rpc_sign_show_fees-28					0a4470afd87	last=47b2ba29df2 !origin-pull/12911/head
	(CHECK-LAST)	last=8bf1fed8415 rpc_sign_show_fees
		# Dropped rel notes file
		# NOTE: Originally #12911
		#28.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e); most of a fix in stash 835c2d3afba
	# Needs review and care (new index): 13014 jonasschnelli/2018/04/txindex_prune
	# Needs work: 13947 Dandelion transaction relay (BIP 156)
	# Needs work: 13989 add avx512 instrinsic
	# Needs review: 13990 WIP: allow fee estimation to work with lower fees
	# Needs review: 14035 Utxoscriptindex
	# Needs work: 14053 Add address-based index (attempt 4?)
	# Needs IN-DEPTH review: 14079 Implement sighash cache in CHECKMULTISIG
	# Needs review: 15093 rpc: Change importwallet to return additional errors
	# Needs review: 15169 sdaftuar:2018-12-parallel-mempool-scriptchecks
	# Needs review: 15204 promag:2019-01-openexternalwallet
	# WIP: 15307 jnewbery/wallet_tool_zaptxs_salvage
	# Needs review: 15414 [wallet] allow adding pubkeys from imported private keys to keypool
	# Needs review: 15424 Sjors:2019/02/wallet_tool_remove_metadata
	# Needs review/finalisation: 15493 rfc: Add -printconfig arg to bitcoind
	# Needs review: 15502 ajtowns:201902-trytoavoiddns
	# Needs review/concept ACK: 15572 Add auto select custom fee when smart fee not initialized.
	15836 fee_histogram+pr15836_api-28			b891a04599d	last=b94292a7cb jonasschnelli/2019/04/feeinfo
	(CHECK-LAST)	last=c5e53d0d21f origin-pull/21422/head
	(CHECK-LAST)	last=f818d33bd5b fee_histogram+pr15836_api
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ? (or not, since it's been abandoned...)
		# TODO: Drop ec2326304e0 since it's not needed with changes made in 998c34d27e7
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
		# TODO: https://twitter.com/RandyMcMillan/status/1490107008443457538?t=Qc4LO63rRuWxErtRel06EQ&s=19
		# 			aka 4613c88c91f4f3846aa62c929ad73d1a3e6ac70e
	22693 getaddressinfo_txids					1bd683de231
	g562  wallet_warn_reuse_gui					ea957a557d1
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# Needs work? 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				a5e45fc1e04	last=a0d0807abc2 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		91423f64d13
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-27+knots		c0fdaeab4d3	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr-28				3f3877f4745	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
	(CHECK-LAST)	last= rpc_dumptxoutset_hr-29+knots
	(CHECK-LAST)	last= compat_rpc_dumptxoutset_hr
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend-28							4d64e9e4a9d	last=b6ca5e9f0c9 uaappend
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks-28						d8114ff1102	last=162f0dba2f2 prune_locks
		# Consider accepting #34534's changes or rebasing on it
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	19873 mempressure-27						2fc6668792f	last=0802d0b4dc1 mempressure
		BROKEN: Linux available memory detection no longer correct; we have different kinds of flushes now; and we need to ensure the OS can actually reclaim the freed memory
		TODO: knots#219
		TODO: knots#295
		# TODO: LevelDB flushing causes burst of memory usage; consider that here; see #31645
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			ad22a24eb7f	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-28+knots				a22e5867430	last=1002e2d0d7f jonatack/setfeerate
	# OR (evaluate): 31278 -  # wallet, rpc: Settxfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-28+knots					59ccec74959	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
	(CHECK-LAST)	last=a5e24757585 rpcauthfile-29+knots
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	# Needs polishing?? 35198 arejula27/truncate_header_sync_percentage
	g149  intro_assumevalid-28					1a80144445f	last= intro_assumevalid
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					34b69da3162	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	g363  qt_peers_directionarrow-25+knots		e5d5a5f6965	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
		FIXME: dfaf5c9e216 Bugfix: GUI: Peers: A single "x" was insufficient for byte-size widths
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						d6140f3cc84	last=1af20831806 Sjors/2021/05/hww-toggle
	# Needs work? 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21260 rpcwallet_tx_in_mempool-28+knots		3be97e6ce15	last=46bf0b7b5d8
	(CHECK-LAST)	last=86f76777c6b rpcwallet_tx_in_mempool-29+knots
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					27405046523
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool-28						97b67babbee	last=040b280c661 rebroad/MaxMempoolRPC
	(CHECK-LAST)	last=771e99c7466 rpc_maxmempool
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex-28						6e151c3f60d	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
	(CHECK-LAST)	last=aaa366361f7 autoreindex-29
	(CHECK-LAST)	last=aaa366361f7 autoreindex-29+knots
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	22159 conf_append_cxxflags-23				a060ae018ee	last=fa14c6818f4
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				86efc23e6b0	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Needs work? 34438 w0xlt/gethdkey
		# WAS: Too many TODOs: 22341 Sjors/2021/06/getxpub
			# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							73691fbf13a
	24963 rpc_walletprocesspsbt_options-26		7c2fb8de207	last=40143bafb52 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
		# Held back f43f992b731...40143bafb52:
			#* 40143bafb52 QA: rpc_psbt: Test that the wrong type cannot be given to named params
			#* 7cd0315bc40 RPC: Strictly enforce the type of parameters passed by name
	-     rpc_descriptorprocesspsbt_opts		3537e02c19c
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# Needs review: 25621 -  # rpc/wallet: Add details and duplicate section for simulaterawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Needs BIP? 22838 achow101:multipath-descs
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs review: g410  benthecarman-g/uppercase-uri
	23362 importfromcoldcard-25					98b55ac8e6d	last=8076f8d4c2a hebasto/211025-cc
	(CHECK-LAST)	last=0b7664c0380 importfromcoldcard
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates-28				f20be3bb5b5	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
	(CHECK-LAST)	last=b196c063427 rpc_savefeeestimates-29+knots
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			3b46e6081b7	last=ad431ff5d18
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip-28					1b0204cba37	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
	(CHECK-LAST)	last= qt_traffic_tooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	# Needs work: g866 rebroad-g/trafficgraphwidget-rebased
	# Needs work: k104 rebroad-g/ more traffic graph stuff
	g820  qt_fontsel_qrcodes-27+knots			ce838070845	last=b14c9d0572e qt_fontsel_qrcodes
	# TODO: qt_fontsel_console
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	-     verifymsg_bip137_and_electrum=28		07d4bdba104	last=567a2962f38 verifymsg_bip137_and_electrum
		# NOTE: Fully reverts gui#819 in anticipation of #24058
	24058 bip322-28+knots						c7dd00c6de5	last=29b28d07fa9 kallewoof/202201-bip322
	(CHECK-LAST)	last=61526466dd1 bip322-29+knots
		# gui#819 fully reverted above in anticipation of this
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-26			d9cb2a45b96	last=97a69e232be
	(CHECK-LAST)	last=f8424c940cc rpc_deriveaddr_wo_checksum-29
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	Needs review: 24539   # Add a "tx output spender" index (txospender)
		# + #34635 ? + #34653 ? + #34747 ? + #34749 ?
		# Check out #34637
	Needs conceptual review: 34636 svanstaa/improve-index-cache-allocation
	# Needs review: 33904 kevkevinpal/feat/rest-gettxspendingprevout
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# TODO? Needs careful review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku ???
	25183 rpc_fundraw_segwitonly				938e4a0ff02	last=9e7fd5c0fe3
	(CHECK-LAST)	last=edf8e63393b origin-pull-k/293/head
		# Currently just an old version for Knots 23.0 compatibility (held back 1c5cfd84b3d...9e7fd5c0fe3)
		# Fixed tests with inspiration from 9e7fd5c0fe3
		# + knots#293
		# TODO: update without breaking compatibility? (new code looks buggy tho - needs rewrite?) (also, filtering by "input type" doesn't really make sense, though segwit filtering does)
	# Needs concept: 25261 -  # rpc: fetch multiple headers in getblockheader()
		# Was: Needs API review: 23330 JeremyRubin/header-fetch
	Needs review: 34299 -  # wallet: re-activate "AmountWithFeeExceedsBalance" error
		# WAS (never in Knots): 25269 -  # wallet: re-activate the not triggered "AmountWithFeeExceedsBalance" error
	# Needs concept review: 25271 jonatack/ConnectNode-say-which-peer-we-are-already-connected-to
		# Concept unsure: Hides logline by default; but maybe we want that with more info included?
	# Needs review: 25366 w0xlt/desc_rpc
		# Besides the private key issue (removed; conceptual issues), RPC doc also has "addresses" where there would be a single address (in a details Object)
	# Needs work: 25434 w0xlt/bypass-timelocks
		# NOTE: Was #21413 glozow/2021-03-bypass-timelocks (never in Knots)
		# Also #25570 ?
	# Needs completion & review: 25718 fjahr/2022-07-allowinbound
	# Needs concept/review: 25747 w0xlt/desc_file
		# If merged, consider multiwallet_rpc restrictions
	# Needs work: 25776 1440000bytes/bumpfee-inputs
	# Needs work: 25923 jonatack/2022-08-statestats
	# Needs Core release first (wallet format change): 25991 wallet_foreign_outputs_metadata
		# TODO: When Core merges it, we can add GUI in Knots right away
	# Needs review (or leave external?): 26052 -  # contrib: Add script to colorize logs
	# Needs review: 26114 -  # net: Make AddrFetch connections to fixed seeds
	# Minimised: 26162 Sjors/2022/09/taproot
	#28.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	# Needs review: 26174 w0xlt/list_address_book
	-     whitelist_outgoing_auto				ec174daacb5
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	a7335c387e0	last=d8434da3c14
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 rpc_disconnectnode_subnet				dfea58ac00a	last=23f4c2cb452 brunoerg/2022-11-disconnectnode-subnet
		# Refactored tests (to be more deterministic) and added support for disconnecting a single IP without subnet specified
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	26990 cli_mw_errormsgs_pr26990-24			73a8f2cce9a
	27034 rpc_importaddr_for_descwallet-27+k	3422369f448	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	27052 rpc_getpeerinfo_lastblockann-28					last=f7788f66b41 LarryRuane/2023-02-getpeerinfo
		# Avoided changing internal data structures
	27216 rpc_getaddressinfo_isactive-28		707ebbb6788	last=85f83339dda pinheadmz/used-addr-ui
	(CHECK-LAST)	last=8eb77c47421 rpc_getaddressinfo_isactive
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-28+knots						64f3666c9e7	last=91771366a3d apoelstra/2023-03--codex32
	(CHECK-LAST)	last=b34e02d766a codex32-29+knots
		TODO: + knots#267
		# See #32652 if #29136 is merged
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	# Needs concept & review: 33043 w0xlt/codex32
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	27600 p2p_forceinbound-28+knots				99edcfd9930	last=8c2026848da pinheadmz/whitebind-evict
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-28+knots			a31727f8451	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	(CHECK-LAST)	last=1543c870273 origin-pull-k/294/head
		# + knots#294
	#28.xTODO# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
	# Needs review & BIP finality & might have wallet changes: 28202 josibake/implement-bip352-receiving
		# Note alternative (approach NACK'd) in #28453
		# OR #32966 Eunovo:2025-implement-bip352-receiving
	# Needs review & BIP finality: 27827 josibake/silent-payments-base-pr-slim-down
	# Needs review & concept: 28241 Sjors/2023/08/silent-index
	# NOTE: If adding new output types (eg, Silent Payments?), need #33065 (rpc, wallet: replace remaining hardcoded output types with FormatAllOutputTypes)
	# Needs review: 27837 furszy/2023_introduce_block_request_tracker
		# Prior work & maybe has an anti-feature?: 27836 furszy/2023_rpc_fetchblock_improvements
	# Needs work: 27854 -  # [WIP] add a stratum v2 template provider
		# OR #28983 OR #29432 OR #30315+???
	# Needs review & compat checking: 27859 -  # Mempool: persist mempoolminfee accross restarts
	# Needs review: g753 -  # Add new "address type" column to the "receiving tab" address book page
	# Needs review and concept: 28463 mzumsande/202308_increase_block_relay
		# Why not just increase inbound capacity to max anyway?
	# Needs review? 28792 (asmap)
		# + update asmap data (see #34696)
	# Needs review: 33920 fjahr/2025-11-asmap-export
	# Needs concept/review? 28806 ajtowns/202311-depinfo-scriptflags
	# Needs concept/review: g777 -  # gui: getrawtransaction implementation
	# Needs concept/review: 28930 -  # wallet: Add scan_utxo option to getbalances RPC
	# Needs review and/or optionality: 28977 murchandamus/2023-11-gutter-guard-selector
	29016 rpc_listmempooltxs-28+knots			8bc551ae426	last=07008477b81 niftynei/nifty/listmempoolentry
	(CHECK-LAST)	last=f7066357360 rpc_listmempooltxs-29+knots
		TODO: Add 29.x bugfix to handle parse error in REST code
		# Includes typo fixup in comment that annoys linter
	# Needs review? 29054 achow101/descriptor-sethdseed
	# Needs concept + review: 29129 brunoerg/2023-12-externalsigner-account-parameter
	# Needs review or minimal impact: 29136 achow101/sethdseed-void-descriptor
		# See #32652 if merged
		# Also #32861 ??
	# Needs final interface: 29163 rpc_help_detail-22								last=c6b68c29707 LarryRuane/2024-01-help-detailed
	# or (newer): 29163 rpc_helpdetail-24									last=56830469303 LarryRuane/2024-01-help-detailed
		# Left off top commit changing rpc_help test behaviour
	# Needs concept & review: 29278 -  # RPC: Wallet: Add maxfeerate and maxburnamount startup option
	# Needs work: 29396 -  # rpc: getdescriptorinfo also returns normalized descriptor
	# Needs review: 29415 vasild/private_broadcast
		# TODO: Extend RPC to allow overriding private broadcast config option
		# + #34267 ? + #34271 ? + #34300 ? + #34322 ? + #34329 ? + #34533 ? + #34646 ? + #34707 ? + #34873 ? + #35016 ? + #35032 (31.x backport in #35046) ? + #35090 ? + #35129 ?
	# Needs #29415 & review: 34457 w0xlt/wprv_29012
	# Needs concept/review: 28926 willcl-ark/2023-07-getnetmsgstats (OR...)
		# Was #27534 -  # rpc: add 'getnetmsgstats', new rpc to view network message statistics
	# Buggy & maybe waste of RAM? Needs review?? 29418 vasild/getnetmsgstats
	# Needs concept & work: 29468 -  # rpc: method removeprunedfunds should take an array of txids
	# TODO: 29553 fjahr/2024-03-dumptxoutset-height
		# +31478
	-     manpages_seealso_notself				b4f685cd288
		# Originally bundled into #29585
	# ----- MUSIG2 -----
	# TODO: 31247 achow101/musig2-psbt
		# +#34010 rkrux/musig-key-fix
		# +Triage: Needs review: 34219 -  # psbt: validate pubkeys in MuSig2 pubnonce/partial sig deserialization
			# NOTE: 30.x backport in #34689
	# Needs review: 33665 rkrux/musig-sighash
	# Needs review & wallet compat check: 31244 achow101/musig2-desc
		# Needs #3313 too?
	# Needs review: 32724 w0xlt/musig2_tests
	# Needs review & wallet compat check: 29675 achow101/musig2
	Triage: 34141 achow101/musig-miniscript
	Needs review: 34697 shuv-amp/fix-musig-descriptor-dupkey
	Needs review: 35154 trail-of-forks/security/fix-signmusig2-psbt-assert
	Needs review: 35155 trail-of-forks/security/fix-setmusig2-secnonce-assert
	# ----- END OF MUSIG2 -----
	29686 manpage_desc-28+knots					6fee3558663	last=47f50c7af55 willcl-ark/manpage-desc
		# Various fixups
	#29.xTODO# 29954 rpc_getmpinfo_policy_pr29954-28+knots				last=d165ac8779b kristapsk/getmempoolinfo-permitbaremultisig-maxdatacarriersize
		# Or maybe this is unnecessary with a get/set policy RPC method?
	#29.xTODO# -     rpc_getmpinfo_policy_coreetc-28+knots
	# Needs review: 29959 laanwj/2024-04-qtsowrap-wayland (needs also #29923)
	#28.xTODO# Split from NAT-PMP removal? 30043 laanwj/2024-05-pcp
		+#33311 laanwj/2025-10-pcp-logging
		+#33338 TheCharlatan/pcp_interrupt (diff-minimise)
	30183 rpc_asmap_followup_pr30183-28			5d05d456bab
	# Needs review: 30080 -  # wallet: add coin selection parameter add_excess_to_recipient_position for changeless txs with excess that would be added to fees
	# Needs review & Core release (wallet format): 30243 -  # Tr partial descriptors
	#29.xTODO# Needs concept? 30341 willcl-ark/psbt-strip-derivs-combine
	# Needs concept? 30381 willcl-ark/addnode-failure
	# Needs review: 30433 fanquake/standard_branch_fedora
	# Needs review? g832 -  # Improve user dialog when signing multisig psbts
	# Needs review/optional? 30572 ariard/reject-unsolicited-txn
		# Was #21224
	TODO: 30595(+34986) + 33791 + 33796 + 33822 + 33825 + 34401 + 34982 + 35187 + 35189?  libbitcoinkernel C API
	Needs rewrite? 30635 Sjors/2024/08/waitforblock
	31121 guix_glibc_cet-28						44b12da4bd8
	# Needs review: 30685 hebasto/240820-control-flow
	30708 rpc_getdescriptoractivity-28			9165f95006a	last=37a5c5d8366 jamesob/2024-08-getdescriptoractivity
	30713 rpc_scanblocks_status_results-28		15e73d0eb8f	last=5b2d0216d87
	# Needs work? 30727 jonatack/2024-08-add-address-type-to-getaddressinfo
	30793 rpc_getorphantxs-28+knots				ad863b5a7ba
		#+31040+31043
		# Includes warning about (unfixable) broken vsize field (abb1cc09785)
	30860 bashcomp_bcli_generate-28				7a279182b1f	last=abf6ad42bdb BrandonOdiwuor/bash-completion
	(CHECK-LAST)	last=af6f73734e2 bashcomp_bcli_generate-29
		# Bugfix + Left off re-generation until later
	k190  -														last=cfc9f871ca3  # Add zsh completion script generation support
		TODO: Ensure added to distdir like in 30860
		# NOTE: Core alternatives in #33402 and #34906
	Needs work: k199 mstampfer/cmake-zsh-completion-only
	Needs Knots-specific work: 34721 willcl-ark/cmake-shell-completions
	30886 rpc_descrprocesspsbt_prevtxs-28+knots	1764e95f94c	last=87ceb610a72 instagibbs/2024-09-updateutxo_psbt
		# Avoided doc-code move
		Alternative: Needs review? 34992 bittoby/rpc-utxoupdatepsbt-add-prev-txs
	30930 netinfo_svcs_outonly-28				c4dd1db3f36
	# Needs work: 31086 dnsseed_cdecker-28								last=5b823920836 cdecker/202442-re-add-bitcoinstats-seed
	31215 http_inc_thr16_wq64-27				d54c2bacb8f	last=e56fc7ce6a9 vasild/rpcthreads
		# Rewrote as only changing defaults (no doc changes)
	# Needs work? 31252 rpc_TxToUniv_witScript-28								last=4e128d4f9b2
		# Alternative: 31256 naiyoma/feature/rpc-show-redeemscript-in-P2WSH-and-P2SH
	# Needs concept ACK: 31353 jonatack/2024-11-total-wallet-balance
	# Needs concept ACK: 31397 glozow/2024-11-multi-orphan
		#+31666
MERGED	31407 macos_notarization-28					530a83a27bf	last=e181bda061c achow101/macos-notarization
		# Left out output renames
		# Left out Windows changes
		# Left off (signer-specific) doc update
		NOTE: Core backport in #32563
		TODO? +#32735
	31531 rpc_signet_info-28					fc177a6170d
	31534 log_big_utxo_flush-26					8de796420d4
	31560 rpc_dumptxoutset_fifo-23				27874e8290b	last=4c8e9b4f35b theStack/202412-dumptxoutset-allow_write_to_named_pipe
	(CHECK-LAST)	last=f9b2197e7df rpc_dumptxoutset_fifo-29+knots
		# Only the FIFO capability, left out the bundled scripts
	# Too convoluted/pointless? Needs review? (Part of??) 31583 Sjors/2024/12/gettarget
		# +33446 Sjors/2025/09/getblock-target
			# 29.x backport in #33474
	# Needs work? 31668 -  # Added rescan option for import descriptors
	31672 peer_cpu_load-28+knots				dee920da09d	last=0f68c47e931 vasild/peer_cpu_load
	(CHECK-LAST)	last=77473c2e166 peer_cpu_load-29+knots
	31845 pruneduringinit-28+knots				a219cacbf55	last=d4a3abf6d43 pruneduringinit
	(CHECK-LAST)	last=ef00b4adfaa pruneduringinit-29+knots
		# TODO: + knots#158 ?
	31886 netinfo_local_svcs-28+knots			bed89007671	last=724546e28a5 jonatack/2025-02-netinfo-services
	(CHECK-LAST)	last= netinfo_local_svcs-29+knots
	# Needs work: 31936 -  # rpc: Support v3 raw transactions creation
	31953 maflcko/2502-fullrbf-follow-up
		TODO: bumpfee_full_rbf-29+knots has some changes for better compatibility
		# Was: 26454 petertodd/2022-feebump-without-optin
	32200 socks_tor_error_codes-0.18
	# Needs work? 32297 ryanofsky/pr/ipc-cli
	32423 laanwj/2025-05-remove-rpcpassword-deprecation
	Review: 32425 vasild/proxy_per_network
		Release notes in #32727
	32429 doc_rpc_keypoolrefill_pr32429-23
	# Needs work: 32468 -  # rpc: generatetomany
	# Needs concept & review: 32471 -  # Fix listdescriptors true fails with 'Can't get descriptor string' in non-watch-only descriptor wallet
	# Needs review; 32489 achow101/export-watchonly-wallet
	# Needs review: g872 achow101-g/export-watchonly-wallet-gui
	# Needs work: g870 -  # Expose AssumeUTXO Load Snapshot Functionality To The GUI
	# Needs concept & work: 32501 BrandonOdiwuor/removeprunedfunds-array
	# Needs review: 32517 pinheadmz/wallet-gettransaction-ischange
	32540 rest_spenttxouts-26
		# +32842
	# Needs concept review: 32541 -  # index: store per-block transaction locations for efficient lookups
	# Needs review: 32638 l0rinc/l0rinc/read-block-hash-check
	32741 rpc_getpeerinfo_nodeid-28							last=9393b33325e
		# OR #32972 ?
	Review ParseHDKeypath change: Part of: 32784 Sjors/2025/06/gethdkey
	32844 rpc_gettxoutproof_segwit-27+knots					last=23edd3db4f1 rpc_gettxoutproof_segwit
	# WIP: 32857 Sjors/2025/07/no_script_path
	# Needs review: 32896 ishaanam/wallet_v3_txs
		# +#33528 glozow/2025-09-send (30.x backport in #33997)
		# +#34238 instagibbs/2026-01-trucness_reorg
	33004 darosior/2507_natpmp_on_default
	# Needs review & wallet format release: 33008 Sjors/2025/07/bip388-register
	# Needs concept: g882 -  # qt: add shift key modifier to clear command history when clearing the console
	# Needs review: 33191 ajtowns/202508-sendtemplate1
	Minimised: 33230 achow101/cli-strong-or-json
	# Needs work? 33259 rpc_getblockchaininfo_bgvalidation-26				last=c1f545248ea  # rpc, logging: add backgroundvalidation to getblockchaininfo
	# Needs work: 33324 l0rinc/l0rinc/reobfuscate-blocks
	# Needs review: 33336 l0rinc/l0rinc/log-initial-signature-verification-state
	# Needs work? 33353 l0rinc/l0rinc/show-reindex-progress
	# Needs concept & review: 33392 -  # wallet/rpc: add scan_utxoset option to getbalance(s) to verify wallet balance accuracy
	33414 tor_pow-29+knots
		# + #34158 top 2 commits (see fix_torcontrol_maxlinelen-29+knots earlier)
	# Needs review: 33448 ajtowns/202508-reportinvtosend
	# Needs work (new doc only applies to guix bins) & backport: 33451 hebasto/250921-install-docs
	# Don't care about signet: g896 -  # rpcconsole: display signet challenge
	Needs work: 33507 -  # RPC: add sendrawtransactiontopeer
	# Needs concept & compat: 33531 w0xlt/multiple_utxos3
	Needs review: 33540 pablomartin4btc/argsman-GNU-style-command-line-option-parsing
	Needs work: g898 apogio-g/feature-utxo-viewer
	# Needs review/concept: 33631 fjahr/202510-asmap-arg-split OR 33632 fjahr/202510-asmap-arg-improve
	# Needs concept EVEN IF MERGED: 33657 -  # rest: allow reading partial block data from storage
		# +#34074
	# Needs concept & review: 33671 ajtowns/202510-wallet-unconf-bal
	# Needs concept & review: g911  ajtowns-g/202511-wallet-unconf-bal-gui
	# Needs review: 33752 -  # rest: Query predecessor headers using negative count param
	# Needs review: g902 prusnak-g/desktop-file
	# Needs work: g909 waketraindev-g/2025-11-gui-comment-sensitive-commands
	# Needs work: g925 w0xlt-g/hide_conflicted
	Needs work: 34512 Sjors/2026/02/getblockfields
	Needs review: 34606 l0rinc/l0rinc/common-warn-high-swap-usage
	# Needs concept & review: 34640 davidgumberg/2026-02-20-send-minfee-msg
		# last=b77555c8fba backported as 891343f1c57
	Needs review: 34683 willcl-ark/json-rpc-schema
	# Not worth it? 34713 hebasto/260302-qt-mkdir
		# NOTE: 30.x backport in #34689
	# Not worth it? 34759 theStack/202603-walletdb-clear_out_secret_data
	Needs review: 34765 overcookedpanda/fix-analyzepsbt-invalid-sig
	34776 hodlinator/2026/03/guix_clean_destructive
		NOTE: 31.x backport in #34800
	Needs concept & review: 34829 chriszeng1010/rpc-getrawtransaction-wtxid
	Needs concept & review: 34933 davidgumberg/2026-03-26-dont-disconnect-unknown-block-hash-cfilters
	Needs concept & review: 35004 HowHsu/usdt-txgraph-tracing-v2
	Needs review: 35006 torkelrogstad/2026-04-05-request-id
	Needs concept & review: 35009 alfonsoromanz/wallet-listtransactions-include-change
	35076 doc_pruning_impact_pr35076-24						last=51ee8ca1683
	Needs work: 35113 optout21/block-dl
	Needs BIP & review: 35221 ajtowns/202604-bip434-support
	Needs concept & review: 35224 kevkevinpal/importDescriptorsPrintoutRequestOnFailure
	-     qt_createunsigned_use_psbtops
		# NOTE: invisible (unmerged) dependency on qt_dialogs_less_modal
	# TODO: Some RPC way to report if settings are default?
	# TODO: sats/vB feerate in GUI: https://x.com/billsmith4lyfe/status/1869097896823713819?t=DH2Z02nl6V_nTQp5znmbgA&s=09
	# TODO: "I have a UPS" mode to avoid flushing frequently even while pruning
	
	# TODO: GUI block template view
	# TODO: Build next-block template from mempool + N MB txs (to replace empty blocks for local miner)
	# TODO: Extend IsUnspendable safely
		# eg based on https://github.com/bitcoin/bitcoin/pull/29981
	# TODO: IPv6 Pinholing (see #30005)
# Non-progress functionality:
	8751  sort-multisigs-28+knots				ffec05ceed7	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					17e4ef3f960	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys-28+knots					647dcf1fe7c	last=0aa860b1252 sweepprivkeys-29+knots
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
		TODO: knots#296
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice-28								20f5b5a0563	last=4a7ed04bd31 ionice
		# low prio: p2p requests, loading/verifying blocks on disk
		# normal prio: connecting blocks, indexes, user requests
	-    ionice_win-28							990ff83c56d	last=930bb1f2fd0 ionice_win
	8501  old_stats_rpc-28						8646f7adcf9	last=7af0ea43b2
	(CHECK-LAST)	last=904b263379c old_stats_rpc-29
		TODO: knots#226
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-28+knots					2872a2809b7	last=63fb11652f
	(CHECK-LAST)	last=7bc611f349b old_stats_qt-29+knots
		# Held back on old version due to conflict with RPC updates...
	9504  rpc_dumpmasterprivkey					66ac57716a1	last=07fc81109a
	g444  gui_netwatch-28+knots					9feaec422dd	last=91ef160f2f8 gui_netwatch-29+knots
		# NOTE: Was #9849
		# NOTE: Includes #25050
	10615 multiwallet_rpc-28+knots				962511f17b4	last=ebaa07fa9c9 multiwallet_rpc-29+knots
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet to wallet-restricted users for now
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
	10554 zmq_wtx-28+knots						560ef5631a7	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
	(CHECK-LAST)	last=4a41f9baa29 zmq_wtx-29+knots
		# Extended doc/zmq a bit to match additions from #14060 and #23471
	20551 rpc_onetry_conntype					fbc15697b73
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment-28			79e3ebd76a0	last=aba8cb28cba relax_invblk_punishment
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
	10350 filtered_witblock-28				eb6c081439c	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				5182926cb3a	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee-28							e74bda85570	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
	(CHECK-LAST)	last=d3e8c5826df rest_fee
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			5f71b8ff12b
	12965 scriptthreads-28+knots				44636605244	last=dfab6c6866 jonasschnelli/2018/04/svt
	(CHECK-LAST)	last=2fc8f747b66 scriptthreads-29+knots
	13203 dsha256_power8-27						f79f994ac5c	last=3b402e0738 TheBlueMatt/2018-05-asm
	(CHECK-LAST)	last= dsha256_power8-29
		# NOTE: Stripped out benchmark change
		#29.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	-     dsha256_power8_asm_pragmas-27			9a6be594a70
	15218 postibd_flush-28						f6400ffc581	last=8887d28a014  andrewtoth/flush-after-ibd
	15428 tor_gui_pairing-28+knots				ea31fd84e38	last=0fbe6e9c46b tor_gui_pairing-29+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-28+knots				0ef06937110	last=1c95be5e3ab tor_subprocess-29+knots
		# FIXME: fix automatic tor outbound using subprocess
		# FIXME: -netinfo doesn't show tor if inbound-only?
	# TODO: tor guix bundle!
	#29.xTODO# 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support TRUC & Knots policies
	17795 gui_console_ctrl_d-26+knots			114b7254d11
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning-28				637b1c54da5	last=c17e9d41d51 restore_vbits_warning
	g537  gui_bech32_errpos						a574710c9f4
	17636 guisettings-0.21						c9fcd4a9cf5	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					612e113fcd4	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						9468bae9ef4	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances-28+knots		e937882a240	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	(CHECK-LAST)	last=ddd1c027a26 cli_getinfo_mwbalances-29
	19092 cli_getinfo_mw_total_balance-28+knots	0e6607f372d	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=fb17d9a2515 cli_getinfo_mw_total_balance-29+knots
	19117 rpc_getrpcwhitelist					fcb36072f90
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-28+knots		a7aa33ccc74	last=14bda42efd0 getrpcwhitelist_wallets-28+knots
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-28+knots		8f9f124c11f	last=afd2785f2c4 wallettool_dump_warning-29+knots
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan-g/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	# Needs concept & review: Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
	30951 v2onlyclearnet-28+knots				8bcb122421f	last=5e3fa6758ba
		# Made a hidden option
	(CHECK-LAST)	last= v2onlyclearnet-29+knots
	# Needs review: 32065 vasild/i2p_early_create_session
	# Needs review & concept: 32726,32728 -  # Add initial OpenAPI/Swagger specification for Bitcoin Core RPC and REST interfaces
	# Needs review: 33044 fanquake/19513_rebased
	# Needs concept & review: 35027 8144225309/net-bind-outgoing
	# Needs concept & review: 35054 fjahr/2026-02-utxo-set-share-safe-take-2
	-     font_for_money_global
	k157  qt_darkmode-29+knots								last=2c15a2071f6 bigshiny90/v29.1-knots-rc1-guifixes
	(CHECK-LAST)	last=62bfaa5132b bigshiny90/gui-darkmode-updates  # knots#160
	# TODO: validaterawtransaction with UTXO lookup (and fee calc) ?
	# TODO: Guix: When glibc 2.36+ is required, use -Wl,-z,pack-relative-relocs
# Non-upstreamed functionality:
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	#29.xTODO# revert #31130+#31157+#31198?+#31916? to restore miniupnpc support
	n/a   restore_feefilter_opt					cf49d58bff4
	-     gui_payreq_textedit-25				b487f357bb4	last=bbd7c7122e3 gui_payreq_textedit
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				2e8254fc98f
	-     walletnotify_w_win-27+knots			c892f8b6dbf	# Latest code now
		FIXME: this is broken :(
	14137 win_taskbar_progress-28+knots			87fe75f61fc	last=18eb4dbb8a
	(CHECK-LAST)	last= win_taskbar_progress
		# NOTE: Could drop /official_releases/archive/ change, but keeping it ensures a conflict when the version gets bumped, so we can update the sha256 hash
	-     restore_blockmaxsize-28				a0a7a60212a	last= restore_blockmaxsize
	7107  qtnetworkport-28+knots				77f2e52bf26	last=1f37c87d8f2 origin-pull/7107/head
	(CHECK-LAST)	last= qtnetworkport-29.1+knots
		# FIXME: Unbind IPv6 on the other port, if its IPv4 bind failed
	7533  sendraw_force-28+knots				9d121259d75 last=2627c0937f8 sendraw_force
	(CHECK-LAST)	last= sendraw_force-29+knots
		# NOTE: overriding anchor-not-empty does not require also overriding non-mandatory-script-verify-flag-upgradable-witness_program UNLESS RDTS is also merged
		#28.xTODO# Allow overriding upgradable stuff (to cleanup segwit abuse spam)
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
		# TODO: 1d3fdc1adde Support ignoring various rejection reasons in PackageMempoolChecks
			# error message change impacts a bunch of functional tests; and submitpackage currently lacks support for ignore_rejects anyway
	11082 rwconf-27+knots						c90495c624f last=130902c94df rwconf-29+knots
		#29.xTODO# Squash fixes
		#28.xTODO# Deprecate with settings.json better?
	7510  rwconf_gui-28+knots					3c18bc835f5	last= rwconf_gui-29.1+knots
		#29.xTODO# Squash fixes
		#29.xTODO# Move blockreconstructionextratxn (and others?) from rwconf_policy?
		# TODO: when we can enable block filters post-pruning, revert 81d696e132c
	559   accept_nonstdtxn-26					e72688bf354	last=2e2f48f871c accept_nonstdtxn
	 929 tbc-25									fe176fa7028	last=32c37e2d493 tbc
		# TODO: Drop ᵇTBC and ˢTBC units for newbies who are getting TBC via tbc_font
		# TODO: Qt6 drops QRegExpValidator
	 553 bugfix_qt_uri_amount_parser-25			55e55d6819c	last=9ada060a060 bugfix_qt_uri_amount_parser
	-     mining_priority-28					07464b13214	last= mining_priority
		#28.xTODO# FIXME: Lots of lock warnings from clang! (did I already fix these?)
		#28.xTODO# FIXME: Should blockmintxfee apply to blockprioritysize??
		# If mempool-knots.dat is ever extended to store easily manipulatable data, port Xor stuff over
		# Reverts (needed and better performance & memusage): d0cd2e804ec [refactor] rewrite BlockAssembler inBlock and failedTx as sets of txids
	5861 gui_restore_addresses					39668f36473
	5891  qt_console_history_persist			76638518995	last=d7bc5138e19 qt_console_history_persist
	(CHECK-LAST)	last=6a5537ab675 origin-pull-k/203/head
		# Includes knots#203 (Add migratewallet RPC in historyFilter)
	Review: k214 kwsantiago/kwsantiago/204-clearhistory
	7219  rbf_opts-28+knots						a1e42756c14	last= rbf_opts-29+knots
		#29.xTODO: Revert #30592
		TODO: Adapt #31953
	-     truc_opts-28+knots					7b898f1d017	last=590417252ab truc_opts-29.2+knots
	-     net_identify_librerelay
	-     net_identify_utreexo
	-     net_identify_rdts
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2-28					b7643238b1f	last=2733d2c4ce7 opt_wallet_segwit2
		# TODO: Split out legacy address preference to be more explicit
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname_wo_dat			1d45ac88ee0	# Latest code now
	-     gui_request_payment_label-0.19		11a5aae7341
	-     gui_peers_sort_network-23				d69b756c939
	-     gui_peers_no_net_column-28			56925da3aeb	last=df6a2e1a9b5 gui_peers_no_net_column
	# 22439 guix_in_gitian-23+knots				2014b1271e3	last=ebda0463748 achow101/guix-in-gitian
		# FIXME: If restoring, test that this still works (WIP fixes in stash fa8517a9112 but need rebase too)
	-     rpc_getblockfrompeer_future			e7c08467524
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		b7fb698aa73
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	-     gbt_rpc_options-28+knots				dc8fc35fc01
	(CHECK-LAST)	last= mining_avoid_block_copy  # core#32547 is included here in 28.x
	(CHECK-LAST)	last= gbt_rpc_options-29+knots
	# TODO: pre-cache GBT call after new block?
	#28.xTODO# RPC to get/set policy configs
		# https://github.com/bitcoinknots/bitcoin/issues/115
	#29.xTODO# -     miningcbtag-27+knots
		# TODO: add to rwconf_policy: 4b38a3031ab GUI/Options: Add miningcbtag via settings
	-     blockview-28.1+knots					d69357dcf51	last= blockview-29+knots
	Needs review? k225  1440000bytes/blockview-txid
	#-     mapport_default_on-27+knots			a32f282230d
		# Re-disabled in light of continued security issues
	#28.xTODO# Look into making the patches tarball in guix
	-     restore_libconsensus-28+knots			57d68d7c5cb	last= restore_libconsensus
		# +Needs review: 24994 hebasto/220426-consensus
	# TODO: bump dbcache to 1 TB on systems we can detect memory pressure! - after testing
		# https://github.com/bitcoinknots/bitcoin/issues/70
	TODO: GUI & first run dbcache setup?
	-     rpccookieperms_log_improvements-28+k	ec34bd875d1	last=198466d5d3e rpccookieperms_log_improvements-29+k
	# Needs work: n/a   macos_dmg-27							d26ae740b99
		# Reverts #28432, #28932, and #28973, and includes fix_dmg_openfinder
		# 28.xTODO: revert macos ZIP only: #29733
		# TODO: Investigate if we can compress again by reverting #24031 using patches in https://bugzilla.mozilla.org/show_bug.cgi?id=935237
		# FIXME: Probably incompatible with #31407 macos_notarization ?
		# TODO? 17311 RandyMcMillan:fix-background-svg
	# Needs review: 31065 danielabrozzoni/20241008_rest_broadcast
	33023 bigshiny90/compactblocks-extratxs-tests-core
	Needs backport: k171  Raimo33/add-dockerfile							last=4b778a21835
	k187  Retropex/dnsseed-leo
	Needs work: k194 -  # gui: Implement two-row status bar with centered progress display
	Needs review? k197 qt_portmap_ux_underlisten
	Needs work: k208 1440000bytes/sendtx-ui
	k262  privkeyio/fix/87-blockfilterindex-pruning-startup	last=08574e0aa23
	Needs concept: k270 privkeyio/compile-tr-native
	Needs work: k274  umop/toggle-banned-peers-visibility
		# NOTE: 7c1a63c0b22 rebased/cleaned up in 31a011d9252, just has extra padding when no bans
	Needs concept & review: k283 cal-gooo/qt-theme-toggle-fusion
	Needs concept & review: k286 Bortlesboat/gui-warn-missing-config
	k288  qt_syncprogressbar_fullwidth-0.7					last=45e89eed5b9 SpectrGen1/issue-177-better-progress-bar
	Review: k297  privkeyio/gui-sweep-privkey
# Non-upstreamed policy options (default off):
	30232 refactor_isstandardtx_mpopts-28+knots	5ba611afd07	last=6ce4823452f refactor_isstandardtx_mpopts-29+knots
	-     pol_acceptunknownwitness
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	29309 permitbarepubkey-28+knots				22193cca113	last=1dfe27e49ab
	(CHECK-LAST)	last=4eb6d39d7cd permitbarepubkey-29+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     bytespersigopstrict-28+knots			9d18c6ea473	last=c86d95dc343 bytespersigopstrict-29+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	9749  unique_spk_mempool-28+knots			84eff5944da	last=b1b8f27e75f unique_spk_mempool-29.2+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     dustdynamic-28+knots					5dd1f1ee25e	last=f10a0071c95 dustdynamic-29.1+knots
	28408 match_more_datacarrier-28+knots		570cb5cb1dc	last=4d2ec0671a3 match_more_datacarrier
	(CHECK-LAST)	last= match_more_datacarrier-29+knots
		#29.xTODO# TODO: Delete TBD "maxdatacarriersize" from #29954 (see b02aab950af) (or at least fix the description)
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# TODO? Revise byte counting to consider input/output waste
	-     datacarriercost-28+knots				42ecf3bfb75	last= datacarriercost-29+knots
		TODO: Review knots#268
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		#28.xTODO# Add tests and make sure boundaries are correct
	k136  pol_permitephemeral
		# Also includes permitbare{anchor,datacarrier} options
		# FIXME: prioritisetransaction shouldn't block dust txs (but also shouldn't blindly bypass policy by promoting ephemeral to non-ephemeral!)
	# TODO: Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	# TODO: Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
		# https://github.com/bitcoinknots/bitcoin/issues/113
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     acceptnonstddatacarrier-28+knots		48c848e044a	last=6a2d5400ee6 acceptnonstddatacarrier-29+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# FIXME: Data before OP_RETURN (and non-push opcodes??) should count the data as non-standard (but can't predict everything, so wait until there's a need? 75f1652b447)
	-     rejecttokens-28+knots					39ec1308346	last=99cde86f433 rejecttokens-29.1+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just Runes
	k78   rejectparasites-28+knots				6c5ca3ed56c	last=d978324923a
	(CHECK-LAST)	last=11bb4add0bc rejectparasites-29.1+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just CAT-21
		# GUI component & default-on moved into rwconf_policy below
		# Rewrote unit test to be more comprehensive
	# TODO: #30964 & LR alternative options
	# TODO: NO APPARENT USAGE: filter HG: https://pbs.twimg.com/media/GDV-H8UWkAAsckl?format=jpg&name=large
	# TODO: CBRC-20 https://twitter.com/bitoordileone/status/1734654996539457666 - INSCRIPTION-WRAPPED: https://mempool.space/tx/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9
	# TODO? All-ASCII data storage (inefficient)
	# TODO? If any input is dust, limit output count to < input count? (or lower?)
	# TODO: Stacks (OP_RETURN X2... - most are 80 bytes long, some 55, few 19)
	# TODO: "OLGA" file storage: https://github.com/mikeinspace/stamps/blob/main/OLGA.md https://github.com/CounterpartyXCP/Forum/blob/1e362f7f8668654d0241fe5b1f1c1c330a8b4368/cip-0033.md
	# TODO? Procedural approve/deny/discount/penalize policy scripting?
		# https://github.com/bitcoinknots/bitcoin/issues/61
	# TODO: k119  Draft: Add support for Lua-based TX filtering
		# Classifier scripts; could be set for valid (dangerous), track for fee estimation, relay, mine, etc
	# Needs concept ACK and review: k107 Retropex/maxfee
	# Needs concept ACK: 29843 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-28+knots				574d3ab59c1	last=edc13c0e6a3 maxscriptsize-29+knots
		#29.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Alternate to(?) #29769
	# Needs concept & impl: Policy: limit script sigops to N (default to MAX_OPS_PER_SCRIPT which is consensus pre-taproot)
	# Needs concept & impl: Policy: limit any witness stack items to N elements (like MAX_STANDARD_P2WSH_STACK_ITEMS)
	# TODO? Ordislow??
	# TODO? Spam filter for stuff like https://mempool.space/tx/4ec38548aa67f6a2efbbc3cf34ab49dc5c275d9701ab0b58696baee9f555c45a
	# TODO: Whitelisting model for non-SPK scripts
	# TODO: -blockpreference=smaller|larger,lessdata|moredata (or match our own policies?)
	# TODO: allow txs from reorg'd-out blocks to bypass policy?
	# TODO: prioritise txs from reorg'd-out blocks?
	# TODO: some way to prioritise Lightning channel activity?
	# TODO? Https://Github.Com/Petertodd/Bitcoin/Commit/04c8e449a34e74e048bf5751d13592a22763ff7e (see email dated 2025-03-19 8:27pm) [bitcoindev] Standard Unstructured Annex
	TODO? Option to reduce effective fee by dust for each anchor/op_ret
	k148  minrelaymaturity-29.1+knots
	Needs review? 32453 JeremyRubin/unsigned_annex
	32521 darosior/2503_nonstd_tx_sigops
		29.x has part in sendraw_force-29.1+knots, rest in pol_maxtxlegacysigops-29.1+knots
	Needs review: 33682 -  # More comprehensive datacarrier configuration
		See also #33690
	# Needs review: 33759 roconnor-blockstream/bip143-standardness-2025-10
	Needs review & optionality: 35225 pinheadmz/p2ms-nonstandard-nonminimal
	-     blockreconstructionextratxnsize
		Consider knots#218
	# Needs review? k221 1440000bytes/getextrapoolinfo-rpc
	# Needs work: k227 1440000bytes/remove-minedtxs-extrapool
	k162  qt_bad_external_signer_msg-22							last=111c401fc5a bigshiny90/fix-invalid-scriptsigner-errordialog
	Needs work: k271  privkeyio/policy-tapscript-dust-limit
	Needs work: k272  privkeyio/policy-subdust-fee-penalty
	Needs review: k275  privkeyio/feature-rbf-feerate-mode
	Needs review: k280  privkeyio/feature-priority-vsize-discount
	k292  Retropex/rework-opnet
	# TODO? Dust multiplier by # of outputs: https://x.com/snapolino/status/1976708308603224518
# Non-upstreamed Knots compatibility:
	n/a   rpc_compat_error_index-25+knots		1ebc7d004d3
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	-     compat_jsonrpc_weirdversions-28		d50d30bf835	last=6cada87972f
	29530 rpc_getpeerinfo_misbehaving_score-28	66b8c669e38	last=87efb6f0cfd
	(CHECK-LAST)	last=e3760287b4c rpc_getpeerinfo_misbehaving_score-29+k
		# NOTE: Held back 976d61c974e...87efb6f0cfd which degrades docs and adds a test incompatible with Knots
		# Deprecated in Knots 28.1
	-     rpccookieperms_octal_compat-28+knots	cbd3aa51b74	last=ce23e2a55e8 rpccookieperms_octal_compat-29+knots
	-     zmq_ipc_uri_compat-28					85f09aa4af0	last=0b1762c90d1 origin-pull/28020/head
	(CHECK-LAST)	last=be5ba1bc7e7 zmq_ipc_uri_compat
		# Backward compatibility with #28020 URI format supported by Knots 25.1+
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-26			dd9a275a37b	last=c6757a7d431 wallet_undeprecate_legacy-29
		# Effectively reverts #24505, #27869, #28597, and gui#764
	14641 fundraw_min_conf_deprecated-25+knots	9e0533bb2c0	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			74f7c944e91
	-     netperms_implicit_addr				9ffb23bb848
	-     rpc_getblockfrompeer_nodeid_compat	925240d6f71
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-25+k		05258006a0a	last=9ceafb77b48 gui_peers_bump_setting_keys-29+k
		#29.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	-    1day_default_conftarget				c189a5677d3
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	# Disabled just to be safe: -     bloom_default-28+knots				401f2f03e86	last=b688158e06d bloom_default-29+knots
		# Take typo fix from def_bloom_local_only
	-     def_bloom_local_only
		# NOTE: Includes typo fix
	-     wallet_avoid_newerchange				5962a67e5f5
	-     enforce_checkpoints					254fabebf5a
	n/a   checkpoint_update-28					41c985132c9	last= checkpoint_update-29
		TODO: update (see #34677 -> knots#291)
		# TODO: Do https://github.com/bitcoin/bitcoin/pull/31940/files ?
	31969 assumeutxo_update-28					d011e71d99c	last=14f16748557 Sjors/2025/03/utxo-880000
	# TODO: revert #28354 ?
	10282 timebomb_knots-28						40f673fe63e	last=84572a8ec93 softwareexpiry
	(CHECK-LAST)	last=2f53648f1a2 privkeyio/fix-gui-datetime-locale
		TODO: + part of knots#336
		Needs work: + knots#247
		TODO: rename branch?
		TODO: disable mining; add alert in advance
		TODO: mention in -help / GUI about ?
		TODO: "OK" is probably the wrong button to use for this
		TODO? "Upgrade" button to open website - or even download+verify??
			-DUPGRADE_COMMAND='...' for PPA/etc?
	-     rwconf_policy-28+knots				6fd67aa463d	last=86056333700 rwconf_policy-29+knots
		# Includes Knots policy changes for simplification of final rebase process
		28.xTODO: revert #33106
		TODO? bump up blockreconstructionextratxn higher? and set a sane blockreconstructionextratxnsize default
		FIXME: LimitOrphanTxSize needs to set m_opts.max_orphan_txs too! (this changed again in 29.x...)
		#TODO: Add segwit wallet stuff?
		#TODO: Get GUI settings for dustdynamic to select ratio box & focus text area when you click their labels
		#29.xTODO# QTreeWidget or similar for GUI Options dialog?
		Needs review: k197 qt_portmap_ux_underlisten (ideally, move this to its own merge, but that requires CreateOptionUI etc split out of rwconf_policy)
		TODO: Increase datacarriersize default
		TODO: knots#245
		TODO: + knots#281
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	# Needs review/options: 26348 -  # Make P2SH redeem script "IF .. PUSH <x> ELSE ... PUSH <y> ENDIF CHECKMULTISIG .. " standard
	# Needs refactoring to only happen for -acceptnonstdtxn(?): 26398 instagibbs/relax_too_small_tx_equality
	# Needs review & optionality: 26451 sdaftuar/2022-11-fixrbf
	# Needs concept & review: k217 1440000bytes/feefilter-extrapool
# SOFTFORK:
	# Disabled: k289  rdts_not_enforced_prompt
	k238 rdts_combined-29+knots								last=f62f5fda667
	(CHECK-LAST)	last=28187c41c8e rdts_consent_prompt
	(CHECK-LAST)	last=d58e6f82909 origin-pull-k/323/head
		# + knots#256 + maxstaleoutbound + maxstaleoutbound=8 + knots#323 + fixes
		# TODO: + updated fixed seeds ?
		# NOTE: Core PR in #24930
	k320  miniscript_guard_tapscript_opif-29				last=74a8dd54ae8 privkeyio/rdts-guard-opif-tapscript
	k348  Retropex/seeds-knots								last=3ca6d37783e
	k350  privkeyio/correct-rdts-invalid-blocks				last=dda6b556b66
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		d4c1e555559
	Triage: 34808 hebasto/260311-qt-ts-source
	7483  svg_icon-28+knots						5b18d9e534b	last=cd64df8af62 svg_icon-29.3+knots
		# Consider: https://github.com/bitcoinknots/bitcoin/pull/54
		FIXME: nsis looks for rendered_icons in srcdir
		TODO: Include knots#328
	n/a   tbc_font-28+knots						458c5339ceb	last= tbc_font
		Triage: fix_qt_fontsel_confusion (bundled in 29.x tbc_font)
		# TODO: Apply font to _all_ amounts when displaying TBC if default font doesn't support Tonal
		# FIXME: Shouldn't be part of branding :/ But depends on the build-for-release-source code from svg_icon...
# BRANDING:
	n/a   copyright_2025-28						19e67dd9efa
		TODO: upd_copyrightyear-29
	n/a   font_ocrbitcoin
	n/a   knots_branding-28						f58950aab87	last=3263c5ee896 knots_branding-29
		#28.xTODO# Review security policy
		FIXME: Add knots#211
		FIXME: contrib/debian/copyright
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#29.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
# TODO: Check that we aren't deprecating anything in Core
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
# TODO: Check that no git Author lines are a mix due to GIT_AUTHOR_NAME no longer allowing emails: git log v27.1.. | grep '^Author.*luke-jr' | grep -v Dashjr
# TODO: test fuzzer with everything enabled
	n/a   (cherrypick=6ee0b3ec0fc)				db9ec3a8f5f	# doc/{bips,files}
		# TODO: Update with bump_version below !!!!
	n/a  (bump_version=Knots:20260507)			ba223403bbc
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist-28+k	45b084a111f	last=34ec626a4fd rm_historical_relnotes_from_dist
	TODO: https://x.com/1440000bytes/status/2009692447040053320
	n/a   (cherrypick=b5bdee81b14)				df2512ca90f  # release notes: write/update, including change log and credits
		# WHEN UPDATING: Remember to check for new authors/co-authors for credits
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge [gk]?\d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
		32425 release notes in #32727
		32521 release notes in #33037 (but not Knots-specific)
	n/a  (cherrypick=20338f1e833)				5f8256608fc  # update manpages (build first)
		# WARNING: Don't forget to add zsh completion!
		# also example bitcoin.conf and bitcoin-cli bash-completion
	#29.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: Upload to Transifex with * d9411324066 (ts_20220515, origin-pull-g/599/head) GUI: Support translating Bitcoin units
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @28.x-knots-android

# TODO: @28.x-knots-extratests
	# TODO: Do both: 30913 maflcko/2409-ci-m1
	# TODO: 31367 dergoegge/2024-11-ci-ulimit-s
	# TODO: 31406 brunoerg/2024-12-fix-test-p2pcompactblocks
	# TODO: 31410 hebasto/241203-multiwallet
	# TODO: 33180 fanquake/asan_strict_string
	# TODO: 34709 rkrux/wallet-tests
	# TODO: 34725 darosior/2603_psbt_roundtrip
	# TODO: 34813 davidgumberg/2026-03-11-txmempoolcslockorder
	# TODO: 34939 achow101/waste-fuzz-overflow
		# 31.x backport in #34942
	# TODO: 34958 theStack/202603-test-getblocktemplate-coinbasevalue_full_block_reward
	# TODO: 34970 Sjors/2026/03/pause-mempool-load
	# TODO: 35170 optout21/2604-parse-keypath-legacy
	# TODO: 35179 polespinasa/2026-04-29-testaddimportdescriptorsrpccoverage
