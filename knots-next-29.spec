timestamp 2026-05-07 03:45:44
#lastapply no-merge

#.. checked up to PR #35239 / gui#936 / knots#303

checkout v29.4
@29.x-syslibs
# BUILD BUGS:
	# Needs review: 33550 ryanofsky/pr/winstream
	# Needs review: 33569 l0rinc/l0rinc/throw-by-value
	# Needs review: 33570 l0rinc/l0rinc/environ-mingw
	# Needs review: g899 hebasto-g/251008-deprecated
	# Triage: Partial: 33779 hebasto/251104-force-iwyu-kernel
TM	34093 fix_freebsd15_netlink_warn			f7ce6ba5c2c	last=c1361fc42dd vasild/fix_nlmsg_ok_compilation_fbsd15
	(CHECK-LAST)	last=490cd874a40 origin-pull/34680/head^  # 29.x backport
	k246  fix_boost1.73compat-29				ae8572d21a0
		# https://github.com/bitcoin/bitcoin/issues/34101
	34462 fix_bsd_batchprio-26					cce96b76c4d
	# Triage: Needs review: 34591 hebasto/260214-cmake-macos-cross
	# Needs review: 34953 sha256_sse4_nosanitize_pr34953-29.3				last=fedeff7f201 deadmanoz/fix/gcc-asan-sha256-sse4-only
	# Triage: 35068 ryanofsky/pr/depfind
	-     revert_core_boost1.91fix				f87ee0699d9
	-     compatfix_boost_1.91-28				4850d1086f9
		# Similar to #35175 (but without the regression)
# SYSLIBS:
	2241  sys_leveldb							f1692ea3121	last=bd2be933f26 sys_leveldb-30
		# Related: #32447
		# If https://github.com/bitcoin-core/leveldb-subtree/pull/52 is merged, this should possibly be adapted
	5416  sys_libsecp256k1						535ac7a1dbd	last=0a4a73bb830 sys_libsecp256k1-30
	# TODO: sys_crc32c ??
	# Hopelessly diverged? -     sys_univalue					5a04090dfe1
	# Hopelessly diverged? 7485  sys_univalue_def				30111aa138c
	n/a   rm_minisketch-29+syslibs				8ecdeb704cd	last=0fd60441475 rm_minisketch-30+syslibs
		# Implicitly includes most of #18818
		#30.xTODO# sys_libminisketch
	15155 test_external_bcli					b4094ecc2f3	last=8f25a48c298 test_external_bcli-30
	30997 qt5qt6-29								b19113028ae	last=65319c41ff1 compat_qt5-30
		# Includes parts of gui#861 whitslack/qt6
	g899  qt6compat_invalidateFilter-23			c6778aac021
		# Expanded to cover watch-only filter
	# Broken, and not worth the effort since a Tonal-capable font bundle is nice to have: g216  optional_font
	#Maybe restore: 7339  opt_libevent
	# Meh? 34390 fanquake/tar_override_get_prev
	# If needed: 35080 maflcko/2604-test-time-factor
	n/a   (delete_release_notes_fragments)
@29.x-knotsfixes
# TESTS:
	# If needed: -     ci_knots-26							e2099d64846
	-     lint_relaxer-29+knots					d8011d2e070
	-     nowarn_unreachable-code				8b39588d6ae
	# If needed: -     nowarn_unused-function				45a2e5951ce
	# TODO: 17402 travis_ppc64							95996ba42a0	last=1d684f05341 elichai/2019-11-powerpc64
		# Cirrus WIP at 8e4fd3e729e, but it fails :/
	# TODO: 25160 hebasto/220517-ci
	# Needs review: 26693 -  # build: special instruction check script (checks for non-portable asm in startup code)
	# If needed: -     ci_i686mp_clang15						955f1eeed99
NM	-     ci_gha_makejobs_8						0c570f97c87
	# Needs review: k209 mstampfer/test-feature-block-bad-version-log
	# Only if native Windows CI: 32219 -
		# NOTE: incomplete backport at c939d74b244
	33639 docker_no_cache_gha-29.4				503fd74e62b
	33990 qa_rpc_startingheight-28				06eb2b7cff1	last=52f96cc235d theStack/202512-test-announced_starting_height
	34185 qafix_pruning_wo_wallet-25			94fb526ff8e	last=8fb5e5f41dd brunoerg/2025-12-test-pruning-wout-wallet
	# Only if native Windows CI? 34285 hebasto/260114-windows-pyzmq
	# FreeBSD: 34346 w0xlt/freebsd_high_port_range-again
	# Only if native Windows CI? 34418 hodlinator/2026/01/31409_fix
	n/a   fix_dbcrash_timeout_pr34589part-0.16	c957c634346
		# Part of #34589
	34622 qafix_debuglog_races_pr34622-29.3+k	87e35a24b6c
		# NOTE: Excludes timeout relaxation
	# If needed: 34690 maflcko/2602-test-zmq
		# NOTE: 30.x backport in #34689
	# If needed: 34728 maflcko/2603-test-wallet-assume-sync
	# Needed in 2026 April: 34815 willcl-ark/bump-cirruslabs-actions
		# See also: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
	# Needed in 2027 October (Python 3.16): 34820 maflcko/2603-test-windows-revert
	# If needed: 34914 Sjors/2026/03/deep-sign (CI macOS codesigning)
	35161 qa_merkle_mutated_rv-0.19				8ec31b46d4a	last=ef501a63d9d l0rinc/l0rinc/doc-merkle-root-mutated
		# Test only
	35164 qa_p2sh_sigop_counting-23				4a336a7070d	last=d180b891a29 musaHaruna/test/p2sh-sigop-counting
		# Held back f1884695736...d180b891a29 for no reason
	# Needs concept & review: 35216 hebasto/260505-illumos-bind
	35218 qafix_fuzz_p2sh_offset_pr35218-25		9bba1850d95
# FIXES:
	33433 qafix_rpc_bind_nonloopback_unavail	d13da13ff0c
	13789 asm_bypass_cxxflags					16dba122acd
	(CHECK-LAST)	last=6878dd8f1ab origin-pull-k/309/head
		# + knots#309
	32217 fix_gitdir_foreign					17be5813e9a
		# Was part of #18902
	#30.xTODO# Revert #32220 (cmake: Get rid of undocumented BITCOIN_GENBUILD_NO_GIT environment variable)
	-     relsrc_embed_tagname-29+knots			4d237d45595	last=607a4fddf61 relsrc_embed_tagname-30+knots
		# Was part of #18902
	18427 2020mingwthrd-mini					4e541cbb8e1	 # Latest code now
	18490 bugfix_symcheck_pe_case				e4c79edbc86	last=63b637b3c34 bugfix_symcheck_pe_case-30
	14968 http_bind_error						87aaa26570c	last=7b5e4001f9 laanwj/2018_12_http_bind_error
	-     http_bind_error+extra					3dd25ab657a	last=33dcd1b043b http_bind_error+extra-30
		# NOTE: libevent-copied code more-or-less up to date as of 2025-09-11 112421c8fa4840acd73502f2ab6a674fc025de37 (upstream has added more portable TCP keepalive, setting keepalive interval to 5min, failure if setting keepalive or reusable fail, and merged 1a6dd1ff1b8 but not e8461128b8d,5a067073d77,45dd91f71f4)
	 9524  rpc_pruneblkchain0					5b8b586df0b	last=88883ae13d
	10731 log_more_uacomment					1a96333bf2b
	29614 bufferedfile_fclose					0ae9a0089d2
	14485 fadvise-29+knots						4d325b42954	last=8fe39e158f9 fadvise-30+knots
		# Was #12491
	# Needs review: 21313 fsync_dir_pt2 after PR submitted & reviewed & tested
	# Needs bugfix: -     fsync_dir_win
	-     rpcarg_type_per_name					d968e47d366
	-     fix_rpc_arg_multiname					e48cf6f79aa
	-     bugfix_rpc_getbalance_hacky			d7fd6bed50f	last=d5ac1a2b0b1 bugfix_rpc_getbalance_hacky-30
	# FIX THE BELOW:
	#14602 bugfix_rpc_getbalance_untrusted-0.17				last=cfa948da1c bugfix_rpc_getbalance_untrusted
	#-     bugfix_rpc_getbalance_acctstar-0.17
	#	FIXME: jnewbery found a bug :<
	# Needs review: 24456 dongcarl/2022-02-kirby-p4
		# NOTE: Was #15191 practicalswift:cs_LastBlockFile (never in Knots)
	# Needs review: 15192 practicalswift:validation-cs_main
	# NEEDS REVIEW: 16003 init: an incorrect amount of file descriptors is requested, and a different amount is also asserted -OR- 27539 Empact/2023-04-minimum-file-descriptor-18911
	# Needs review: 16050 promag:2019-05-importmulti-update
	18194 bugfix_gui_edit_sendaddr-mini			9e649530abe	last=0a44e08992f bugfix_gui_edit_sendaddr
		# NOTE: -mini is just missing the last commit :)
	# Needs re-concept: 19358 # net: Make sure we do not override proxy settings in hidden service.
	19419 listwalletdir_skip_data				0f25908e892	last=3f9cc0cd736 Saibato/wallet_351
	(CHECK-LAST)	last=46cd10a4051 listwalletdir_skip_data-30
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
	g152  gui_notify_setup_bg					8a51fffda72
	-     bugfix_gui_drop_abc_confusing_hack	8a208ac5291
	# Needs review: g201  jonatack-g/inbound-block-relay
	# Needs review & bug fixes: 21106 pstratem/2021-02-07-isinitialblockdownload-timeout
	g236  gui_init_walleterror_cont				7c6a8d928ca
	-     rpc_addconnection_mainnet				ea5a0dd44bf
	32343 subproc_closefds						cc95474235d
		# Was #30756
		# Replaces #22417 (Boost::Process variant)
	# Needs review: 22665 darosior:rbf_optin_nomempool
	23027 bugfix_util_test_config				5b33aa5bfb5
	# Needs review: 22913 -  # Fix the case where the peer status is not updated
	# Needs review & concept check: 23074 Package-aware fee estimation
	# Needs work: 32964 w0xlt/r_26573
		# Was #26573 darosior/taproot_over_dont_under_estimate
		# Was #23502 achow101/tr-low-fee-est
	# Needs work: 23534 achow101/no-change-fee-w-sffo
		# NOTE: If we're sending to someone else who is paying the tx fee, it actually makes sense?
	g506  qt_qrcode_sizefixes					f1af553e8ef
	# Needs review: 24034 -  # p2p: delete anchors.dat after trying to connect to that peers
	24066 -										8284cbfd27b	last=89cb2b6d91e  # contrib/init: (OpenRC) use -daemonwait to wait for startup completion
	-     openrc_from_gentoo					53da98006e9
		# Other OpenRC updates from Gentoo:
		# - PIDDIR in /run instead of /var/run
		# - LOGDIR var added
		# - RPC cookie group-readable
	# Needs review: 24090 RandyMcMillan/1642450390-issue-24049 / now #27386
	# TODO: Actual fix for: 24432 -  # test: Check error for non-existent directory symlink
	24479 bugfix_settings_numberval				e8e68a67590
	# Needs review/concept check: 24563 ajtowns:202203-fillpsbt
	# Needs review/triage: 24571 -  # p2p: Prevent block index fingerprinting by sending additional getheaders messages
	24718 fix_rpc_docs_pr24718-28+knots			1429496c887	last=68a041dd12b
	# Needs review: 24827 -  # net: Fix undefined behavior in socket address handling
	# Needs review: 24835 -  # Revert "Do not consider blocked networks local"
	# Needs review: 24912 mruddy/nchaintx_type
	# Needs review: 24972 hebasto/220425-no-libtool
	g595  qt_handle_autostart_errors-0.15		d3ed8b8748f	last=d932157eb79
		# Upstream mruddy-g/issue_24953 repo got deleted :/
	-   gui_psbt_error_msgbox					88bee4f0f90	last=87c42be2d70 gui_psbt_error_msgbox-30
		# WAS: g599  ts_20220515-partial-25				5191aa16ac2	last=d9411324066 ts_20220515
			# NOTE: Partial backport of only beneficial fixes that don't require translators to do something further
			#TsTODO# Update with other commit (unit translations) when translations supported again
	32358 fix_subprocess_pr32358-28				01d4cef49fc
	32567 fix_subprocess_pr32567-28				94176014beb	last=e63a7034f03 hebasto/250520-subprocess-backports
	29868 hww_windows-29						6fc6e0b3b1c	last=3a18075aedd hebasto/240414-win-subprocess
		# NOTE: Retained `ENABLE_EXTERNAL_SIGNER` cmake option
		# Replaces: -     hww_windows-27						e1f9c1bbde8
			# Reverts #29489 & #28967
	# Check on #25561 (nonsense signed int overflow in leveldb?)
	# Bad idea? 25688 fjahr/2022-07-torcontrol
	# Needs review: 25690 fjahr/2022-07-localaddr
	g633  -										574fff234df	last=5fde8fbe085  # qt: Fix shortcut ambiguities
	# Meh: 25854 -  # tracing.md trivial English fixes
	g662  qt_fix_txview_202209					660851022ad	last=7304c97b1af qt_fix_txview_202209-30
		# Includes gui#368
	# Needs triage & review: g666 furszy-g/2022_gui_safe_connect_qtimer
	# TODO: Needs review: 26260 -  # rpc: Set best header after reconsiderblock
	# TODO: Needs review: 26316 andrewtoth/block-read-shared-mutex
	# Needs work? 26343 mzumsande/202210_addrfetch_servicebits
	# TODO: Sane fix for #24049
	g677 fix_qt_peers_na						a8d890d3dcd
	# Needs work: 26534 -  # Fix macOS failing to flush blockfiles to disk for certain external drives
	# Needs work: 26535 mruddy/issue_2039_readonly_finalized_blk_files
	g684  qt_reqs_multiselect_pr684-28+knots	002d65f9ac2	last=a6f567590b7
	(CHECK-LAST)	last=db656379a62 qt_reqs_multiselect_pr684-30+knots
	# Changes wallet format: Needs review? 26728 achow101/wallet-knows-master-key
	# 27231 jonatack/2023-03-logging-fixes-and-test-coverage
		# NOTE: 261b9b766a7 has diff minimisation of (non-refactored) EnableOrDisableLogCategories
	# Not worth deviating from Core? 27277 Sjors/2022/03/log-tx-validation
	#30.xTODO# CAUTION: #27307 was merged, but "this appears to possibly show a higher balance than the user actually has for sure??" - investigate
	# Alternative to: 27434 pinheadmz/chaintips-invalid
	# Needs work/review: 27557 pinheadmz/async-getaddrinfo
	# Needs concept review: 27591 rpc_mempoolvsize-25								last=60bde2dac05 glozow/2023-05-mempool-vsize
		# When restoring, revert part of bfab6ac4791 in relnotes
	# Needs review: 27601 furszy/2023_wallet_double_change_output
	#30.xTODO# Needs review: 26732 furszy/2022_wallet_do_not_select_utxo_from_the_tx_being_replaced
	-     qafix_assert_debug_log_create			db6f711b739
	-     acceptstalefeeestimates_mainnet_opt	1cbd4cd6aae
		# Currently (28.1) needs qafix_assert_debug_log_create
	# Needs review: 27684 hebasto/230516-punish OR ???
	#30.xTODO# Configure-time checks? Needs review: 27731 fjahr/2023-05-fd-exhaust
	# Needs review: 27804 -  # init: deduplicate added connections
	27814 forbid_nohelp-29						4373798ca4d	last=bfc2bb6a270
	# Needs concept/review: 27830 -  # Supporting parameter "h" and "?" in -netinfo.
	# Needs review: 27912 -  # net: run disconnect in I2P thread
	# Needs work: 27973 maflcko/2306-byte-span-
	28029 fix_zmq_errhandling_202307-mini		1dd35f52ee7	last=ba28af94bd5 fix_zmq_errhandling_202307
		# Just diff-minimised
	28055 fix_getblockfrompeer_rereq_err		6c1cb8b6cdb
	# Needs review: 28126 furszy/2023_bugfix_wallet_importaddress
	# Needs review: 28192 Sjors/2023/07/parse-hd-keypath
	# Needs review: 28235 -  # p2p: ensure mapBlockSource is removed from in ProcessBlock
	# Needs review: 28248 jonatack/2023-08-network-diversity
	28345 fix_bytespersigop_checks-mini			e76583cd529	last=6f627727739 fix_bytespersigop_checks
	(CHECK-LAST)	last=cd8ab840ad6 fix_bytespersigop_checks-mini-30
		# Related bug in #18479
	# Needs review: 28395 furszy/2023_coinselection_fix_bnb_upper_bound
	# Needs concept ACK (even if merged): 28488 naumenkogs/2023-9-evict-minfee
	# Needs concept ACK (even if merged): 28538 mzumsande/202309_fullob_to_blocksonly
	# Needs review: 28514 -  # wallet: Fix wallet directory initialization
	# Needs concept review: g762 -  # Update about logo icon (colour) to denote the chain type of the QT instance in About/ Help Message Window/ Dialog
	28616 Sjors/2023/10/assume-unconfirmed		82edb698112	last=3e281590c7d  # assumeutxo_unconfirmed_ux_Sjors-28
	(CHECK-LAST)	last=202163a6778 assumeutxo_unconfirmed_ux_Sjors-30
	-     assumeutxo_unconfirmed_ux-29			a65ea9fe34e	last=ee1bfd9dada assumeutxo_unconfirmed_ux-30
	-     qt_recomm_confirms-0.9				eda24e275f5
		# NOTE: Un-hardcoding 6 already taken care of in assumeutxo_unconfirmed_ux above (956546a1f2f)
	# Needs review & triage: 28678 sipa/202310_miniscript_assume
	# Needs review: g775 -  # gui: add used balance to overview page
	# Needs review: 28780 -  # log: torcontrol opt checks
	-     fix_keep_notmy_cookie					3def5b88fde	last=61678a031e1 fix_keep_notmy_cookie-30
		# Originally part of #28784, but regressed in d95dde9441f...7cb9367157e
	# Needs review: 28824 fix_asm_nodecimals-23								last=fde11cb0fa3 willcl-ark/asm-full-hex
		# FIXME: disambiguate opcodes too?
	28944 rpc_sendall_anti_fee_sniping-28		37bab256c15	last=aac0b6dd79b ishaanam/sendall_anti_fee_sniping
		# + #33118
	# Needs review: 35019 HouseOfHufflepuff/rpc/uniform-locktime-anti-fee-sniping
	-     rpc_walletcfpsbt_antifeesniping-28+k	e57b5ba1cc8	last=6fc07948bdd rpc_walletcfpsbt_antifeesniping-30+k
	(CHECK-LAST)	last=113ba106273 Sjors/2025/07/locktime
		# Includes tests from #32892
	29141 fix_rpcauth_blank						71a1fb9121b
	# Needs work: 29147 guix_attachable_sigs					ad4fe4b83a4
		# GPG discourages clearsign signatures!
		#30.xTODO# but windows has lots of problems with existing style...
		#30.xTODO# but deviating from Core signing may reduce participants?
	# Needs review: 29155 -  # wallet: move lock at the top of ReleaseWallet
	29175 -										04c569a8275	last=be8ae64b82e  # rpc: validate fee estimation mode case insensitive (fix_rpc_estmode_unset_case-24)
	(CHECK-LAST)	last=4a833a7ae11 fix_rpc_estmode_unset_case-30
	# Needs work: g786  -  # FIX:When opening or autoloading wallets there should be clear messages about rescanning in progress and wallets' names.
	31551 bulk_block_rw-29+knots				57ea2496229
		# Optimisation, not fix - but simplifies #29307
	29307 AutoFile_error_check-29+knots			cf279dd4946	last=c10e382d2a3 vasild/AutoFile_error_check
	# Needs work: g792 -  # Correct tooltip wording for watch-only wallets
	# Nothing to fix? 29589 -  # tests: fix OP_1NEGATE handling in CScriptOp
	29640 fix_tiebreak_on_disk-26				0957800bd8d	last=0465574c127 sr-gi/202403-block-tiebreak
	(CHECK-LAST)	last=20ae9b98eab origin-pull/34521/head
		# IMPORTANT: Adds a UB bugfix
		# left off doc change (4caa38600e6)
		# TODO: + #34521 if ready (better UB fix? addresses assumeutxo?)
	#30.xTODO# Needs review: 29652 ryanofsky/pr/noloc
	#30.xTODO# Needs review: 29664 mzumsande/202403_near_tip_stalling
	29678 fix_init_lowdisk_warning_reqd-29		8db9f5499e9	last=b1117e5a716 fix_init_lowdisk_warning_reqd
		# Excluded dev doc update
	# Needs review: 29680 -  # wallet: fix unrelated parent conflict doesn't cause child tx to be marked as conflict
	# Needs review: 29770 fjahr/2024-03-check-undo-index
		# +#34991 ? (31.x backport in #35231)
	# Needs review: 29796 fanquake/depends_0g_debug_flags
	-     fix_rpc_warnings_all-28				d8f8ecfc8aa
	g815  fix_qt_privacy_before_open-23			9d01c387ed4	last=0dc337f73d0
		# Rewrote myself due to overcomplication and race bug in PR
	# Not worth it? 29963 hebasto/240425-guess-cc
	#30.xTODO# Needs review: 30079 ismaelsadeeq/05-2023-ignore-transactions-with-parents
		# Was: 25380 darosior/fee_estimator_disable_cpfp
	-     jonatack/2024-05-fix-cjdns-detection-in-AddNode	977f603bc17	last=be4541abe59 jonatack/2024-05-fix-cjdns-detection-in-AddNode  # fix_cjdns_addnode_detect2-27+knots
	# Needs review: 30155 mzumsande/202405_replay_blocks OR 33442 l0rinc/l0rinc/interrupt-rolling-forward
	#30.xTODO# Revert or semi-revert #30157 ?? (Mempool-influenced fee estimation)
	# Needs review & diff-minimising: 30207 mzumsande/202405_invalid_chains
	30221 fix_wallet_bestblock-29.3				ac094dc6928
		# aka knots#290
		# +#32281 +#32580 +#32345
		# Excluded 30a94b1ab9ae850d55cb9eb606a06890437bc75e (test removal) for diff-minimising
	# Needs work: g823 -  # wallet: Improve error log color in the console
	-     detect_clang_bug96267					3fc4cd42208	last=ea6ae8d271e detect_clang_bug96267-30
	# Needs review: 30359 -  # Correct Error Code in OP_IF/OP_NOTIF Empty Stack Check
	# Needs review: 30469 fjahr/2024-07-csi-overflow-2
		# Was: 26426 fjahr/202210-coinstatsindex-overflow
	# Needs backport: 30479 mzumsande/202407_fix_resetfailure
	# If needed? 30489 theuni/depends-zmq-patch
	# Needs review: 30972 BrandonOdiwuor/wallet-listreceivedby-fix
		# was: 25973 -  # wallet: Filter-out "send" addresses from listreceivedby*
	31275 fix_rpc_example_quoting_pr31275-24	ce38b2d985e	last=7e93e292598
	# Needs work? (adds overhead) 31298 -  # rpc: combinerawtransaction now rejects unmergeable transactions
	# OR: Needs work: 33361 -  # Fix #25980: Validate transactions in combinerawtransaction
	# Needs work: 31349 vasild:test_log_internet_traffic
	# Needs work: 31378 furszy/2024_wallet_migration_multisig_crash
	# Needs review: 31404 furszy/2024_descriptors_infer_multisig
	# Needs careful review: 31405 mzumsande/202411_stricter_invalidblock_handling
		#+32843
	# Needs review/correctness per branch: Diff-minimise: 31449 -  # coins,refactor: Reduce getblockstats RPC UTXO overhead estimation
	#30.xTODO# Revert: Knots NOT AFFECTED: 31453 macos_exfat_warning-29+knots			25f0359c100	last=db3228042b2 willcl-ark/macos-exfat
		# Checking blocksdir unconditionally in case it's a mountpoint
		# Dropped doc change
		# Added warning before leaving GUI firstrun screen
		# Only affects macOS 14.x (13.x and 15.x unaffected)
		# Knots gets rid of likely-buggy macOS-specific AllocateFileRange in fix_preallocate, which fixed this
	31514 fix_wallet_rpc_ranged_pr31514-29		b08cefbc13e
	# Not strictly a bug? 31603 brunoerg/2025-01-descriptor-pk
	# Needs work? 31610 l0rinc/l0rinc/gettransaction-rpc-doc
	# Needs work: 31615 -  # Ensure assumevalid is always used during reindex
	#29.xTODO# 31622 achow101/psbt-sighashes
	31727 miniscript_nonfatal_pr31727-29		5615ebfab13	last=3693e4d6ee0 !hodlinator/2025/04/31727_followup
		# Includes fixes from #32255
	# Needs review? 31734 -  # miniscript: account for all StringType variants in Miniscriptdescriptor::ToString()
	# Needs review? 31774 -  # crypto: Use secure_allocator for AES256_ctx
	# Needs work & importance: 31775 -  # rpc: collect transaction fees on generateblock
	31785 fix_gui_rpcconsole_waitfor-29			bfc79474d0d
	# Needs review: 31807 theuni/fix-dupe-kernel-symbols
	# Is it even a fix? 31829 glozow:2025-01-orphanage-peer-dos
		# CAUTION: Needs backports from #35175 (merged in 29.4 without them)
	# 31912 workaround_buggy_rndrrs-28			36e11bb93cc	last=2498dd8dbd5  # random: Check GetRNDRRS is supported in InitHardwareRand to avoid infinite loop
		# Held back 585aba6eec8..2498dd8dbd5 (2x diff for basically the same thing)
	# Needs review? 31835 -  # validation: set BLOCK_FAILED_CHILD correctly
	# Needs work: 31888 midnightmagic/fix-linearize-gjpyn
	# Needs review: 31929 hodlinator/2025/02/stop_http_robust
	31958 -										0adc81e3948	last=32dcec269bf  # rpc: add cli examples, update docs  # docfix_rpc_wallet_cf_psbt-24
	31979 -										f92f0e01b89	last=f708498293c  # torcontrol: Limit reconnect timeout to max seconds and log delay in whole seconds  # tor_backoff_max-26
	# Needs review: 32051 jonatack/2025-03-addnode-p2p
	32073 netinactive_dont_downgrade-26			3849cedfc2d
	# Needs concept & review: 32123 -  # wallet: make coinbase that will mature on the next block available for selection
	# Needs review: 32143 -  # Fix 11-year-old mis-categorized error code in OP_IF evaluation
	# Needs review: 32159 willcl-ark/pcp-default-multipart
	32176 tor_rnd_stream_isolation-28			b0046014114
		# Omitted renaming variable
	# Needs review: 32180 mzumsande/202403_ibd_lastcommonblock
	32185 fix_dbwrapper_batch_header_size-26	27fbb0e122f
		# Only the fix, without the bumped LevelDB version dep
	# Needs review: 32186 -  # descriptor: handle listdescriptors(private=true) for taproot descriptors having partial keys
	# Needs review: 32199 maflcko/2504-time
	# ----- IN SEQUENCE, NEEDS BACKPORT REVIEW IN #35226 -----
	# Needs backport review: 32602  # fuzz: Add target for coins database
		# Includes first commit of #32279 for #32313
	# Needs backport review: 32313  # coins: fix cachedCoinsUsage accounting in CCoinsViewCache
	# Needs backport review: 34207  # coins/refactor: enforce GetCoin() returns only unspent coins
	# Needs backport review: 34164  # validation: add reusable coins view for ConnectBlock
	# Needs backport review: 33512  # coins: use dirty entry count for flush warnings and disk space checks
		# Adds a tag to the CoinsViewCacheCursor constructor to avoid silent conflicts
		# Diff-minimises entire sequence
	# ----- END SEQUENCE -----
	32344 fix_wallet_nonranged_pr32344-22		caf570fd588	last=97d383af6d5
	32351 qafix_nonrecurs_FindChallenges-28		d2ed43db183
		# Fix only
	32355 fix_block_full_enough-29.3			2fbf429627c
	# Needs review: 32367 hebasto/250428-enable-lang
	-     fix_fs_error_utf8-23					9cd3fc41c4d
		# Alternative to core#32383 hebasto/250429-fs-error
	32414 fix_reidxcs_periodic-25				867b061854d	last=c1e554d3e58 andrewtoth/reindex-flush
		# Fix only
		# TODO: consider performance refactor?
	# Simplified rewrite of? 32528 maflcko/2505-1
		# Was (unreleased) #31135 jonatack/2024-10-verification-progress or #31177 polespinasa/verificationProgress
	32539 fix_rpcallowip_cjdns-29				2f600259bec	last=12ff4be9c72 pinheadmz/rpcallowip-rfc4193
	# Needs work: 32577 hebasto/250521-subprocess-split
		# FIXME: Ensure this gets resolved before #32566 is merged
	#30.xTODO# If #32566 is merged, test extensively with Windows quoting nonsense
	# Needs review: 32606 davidgumberg/5-23-25-ignore-unsolicited
	# Needs review and simplification? 32636 davidgumberg/5-27-2025-create-refactor
		# + fix from #34490
	32682 fix_wallet_fillpsbt_nothrow-28		c5a6d51ab5c
		# Diff-minimised only
	# Needs review: 32685 -  # wallet: Allow read-only database access for info and dump commands
	32736 fix_listwalletdir_err-23				773b1625fce
	# Needs review: 32757 -  # net: Fix Discover() not running when using -bind=0.0.0.0:port
		# Was #31492 (not in any release)
		# Or #33935
	# Needs review: 32773 hebasto/250618-mkdir
	# Needs concept & review: 32788 achow101/desc-allow-H
		# Check for this impacting other Knots merges
	#30.xTODO# Needs review: 32821 -  # rpc: Handle -named argument parsing where '=' character is used
	32845 fix_rpc_nowallet_errors_pr32845-29	9e9121adf6c
	# Needs concept & review: 32869 instagibbs/2025-07-invalid-cb-stall
	32878 fix_index_rewind_badassert_pr32878-19	2c9733d9088
		# Fix only; left off invasive test
	32987 fix_gui_reindex-29					47f2ba54ca0
	# Needs review: 33014 b-l-u-e/fix-32849-descriptorprocesspsbt-internal-bug
	# Needs review: 33072 b-l-u-e/p2p-fix-nscore-overflow-24049
TM	33105 cve2025_46598_pt1-29.1                            34e68a41877
TM	32473 cve2025_46598_pt2-29.1                            8cf2ab34a65
TM	33050 cve2025_46598_pt3-29.1                            17bdf876c0b
	# Part of, if translations are important: 33115 hebasto/250801-ts-files
	# Needs work: 33126 Ataraxia009/multi-client-support
		# NOTE: Rewrote in knots_branding
	# Needs concept/work: 33127 Ataraxia009/launch-crash-failure
	# Needs review: 33135 Sjors/2025/08/older-safety
	# Needs review: 33164 hebasto/250809-fallback-fallocate
		# NOT SUFFICIENT WITHOUT:
	33228 fix_preallocate						bc10a6c23a4
		# Includes less-than-ideal workaround for https://github.com/bitcoin/bitcoin/issues/33128#issuecomment-3203396013
	33215 fix_debuglog_refs_hardcoded-28+knots	7b687341c77
		# Includes gui#884 hebasto-g/250819-debuglog
	# Needs review? 33223 murchandamus/2025-08-tiebreak-SRD
	# Needs work: 33231 w0xlt/mulitple_binds
	# Needs review: 33297 -  # cmake: Inherit WERROR setting for secp256k1 build
	33311 log_quiet_pcp_unsupported-29			ff5bf1aeade
	33338 pcp_interrupt-29						08bb8aa241a
		# Diff-minimised
	# Needs review: 33358 -  # contrib: fix for macOS deployment build failing on Qt translations even though it is optional.
	# Needs review: 33360 -  # rpc: Add validation for invalid taproot signatures in analyzepsbt
	# Needs concept: 33427 john-moffett/rpc-submitpackage-reportall
	# Needs review: 33430 john-moffett/rpc-addpeeraddress-error
	g886  wrkrnd_qt_textedit_oom-0.14			1a482414aff
	# Needs review: 33443 l0rinc/l0rinc/rate-limit-rolling-forward
	# Needs review: 33444 -  # rpc: Fix dumptxoutset rollback with competing forks
	# OR (preferable): 33477 fjahr/202509-better-rollback
	# Needs work? g895  benthecarman-g/fix-dark-mode
	33464 net_timers_for_inbound_inv-29			83a7acc5710
NM	33475 fix_block_full_enough_underflow-29+k	67cdcbcee65	last=b807dfcdc59 ismaelsadeeq/09-2025-miner-infinite-loop-fix
	33494 urlupd_depends_qrencode-28			d3d5f892277	last=93a70a42d30 hebasto/250929-qrencode
		# NOTE: Held back 9dbfce7fc84...93a70a42d30 (which drops package name from download filename) and addressed cache filename issue another way
	# Needs review: 33498 -  # p2p: Mitigate GETADDR fingerprinting by setting address timestamps to a fixed value
	33511 fix_sigint_waitrpcs-29				22ff8f97281	last=c25a5e670b2 ryanofsky/pr/sigwait
		# Held back 68cad90dace...c25a5e670b2 pending more review
		# Kept old notification to workaround GUI console regression
		# 30.x backport in #34192
	# IPC-specific: 33566 Sjors/2025/10/wait-empty-mempool
		# 30.x backport in #33609
	33580 fix_depends_fallback_filename-0.13	a988743cdd1	last=671b774d1b5 achow101/depends-fallback-name
	# Needs review: 33604 -  # p2p: Allow block downloads from peers without snapshot block after assumeutxo validation
	# Needs review: 33616 instagibbs/2025-10-bypass_checkephemeral
	# Needs review: 33646 -  # log: check fclose() results and report safely in logging.cpp
	# Needs review: 33663 -  # addrman, net: Filter during address selection via AddrPolicy to avoid underfill
		# Or #34162 fjahr/2025-12-33663-alt
	# IPC-specific: 33676 ismaelsadeeq/10-2025-add-interruptWaitNext
	33698 fix_qa_rpctimeout_pr33698-27			3f910eb66f7
	# Needs review: 33699 0xB10C/2025-10-addr-token-bucket-start-5
	n/a   restore_dnsseed_luke-jr-29.3			f353f4f7094
		# Reverts #33723
	# Needs review: 33727 -  # zmq: Log bind error at Error level, abort startup on init error
	# IPC-specific: 33745 Sjors/2025/10/submit-solution-doc
		# +#33880
	g901 fix_qt_rpchistoryfilter_pr_g901-28		6bc4b01e82c
	# Needs review: g904 diegoviola-g/fix-qt-wayland-rendering-issue
	# Needs concept: g905 -  # Increase tooltip wrap threshold from 80 to 100 characters
	33813 warn_for_rpcbind_ignored-29			457febc3cfd	last=335a05c69e1 Ataraxia009/rpc-bind-warning
	# Needs review: 33854 -  # fix assumevalid is ignored during reindex
	# MSVC-specific: 33865 hebasto/251112-plugin-path
	33956 fix_p2pv2_useafterfree_pr33956-26		a11cbbe3ac3
	33960 loglevel_corrections-29+knots			6446ff1d740
		# NOTE: Silently dropped a change somewhat equivalent to #33813 (which is GUI-loud)
	-     loglevel_corrections_bdb-29+knots		29bce9ebc76
	# Triage: IPC-specific: Needs review: 33965 Sjors/2025/11/ipc-reserve
	33993 doc_stopatheight_imprecise-21			0811078bdef
	34028 fix_seenlocal_max-26					1ab145725b6	last=2189a6f5f22
	-     fix_feeest_read_rare_overflow-29		71ad39e4210
		# Alternative to: 34109 maflcko/2512-fix-u64
	-     pcp_dont_spam_unauth-29				6ba518998e6
	(CHECK-LAST)	last=af5c2fcf144 origin-pull/34117/head
		# TODO: Consider replacement with #34549
		# Inspired by the first commit on #34117
	# Needs concept/review: 34117-commit-2  net: fix CJDNS address discovery when -externalip is set
	# IPC-specific: Needs review: Partial: 34143 hebasto/251223-boost-layout
	# Needs review: 34146 0xB10C/2025-12-separate-self-announcement
		# + #34297 (p2p: add validation checks for initial self-announcement)
		# + #34717 ?
	# ----- WALLET DELETION BUGFIXES -----
	32273 fix_walletmigrate_relpaths-29.3		2a88b6d4e59
		# NOTE: Held back "wallet: migration: Make backup in walletdir" behaviour change
	34372 qa_wallet_migration_tests_202601-29.3	4f6bb020efb
		# NOTE: Invisible dependencies on #32273 and #34370
	34176 handle_wallet_dir_nonwritable-29.3	282b10c3294	last=08925d5ee75 furszy/2025_wallet_check_db_permissions
		# NOTE: temporarily restored `descriptors=True` in tests until bdb is updated to pass
	-     handle_wallet_dir_nonwritable_bdb-29.3	f729830e3c7
	31423 wallet_migrate_watchonly_only-29.3	855430ccd23
		# NOTE: Includes parts of #32984 and #34156
	# Needs review: 34193 furszy/2026_wallet_safer_MigrateToSQLite
		# NOTE: Backport in 1f17fcee406
	# Needs review: 34198 furszy/2026_wallet_migration_ancient_wallets
	k242 fix_bdb_edge_cases_202601-29			909c5879a8c
	k269 wlt_migrfail_cleanup_lognonempty-29.3	3b0589bc6d5
	# TODO: consider knots#249 review comments
	# ----- END WALLET DELETION BUGFIXES -----
	34161 fix_distance_ub_pr34161-26			dc867bd7a44	last=477c5504e05 l0rinc/l0rinc/pool-allocator-ub
	# IPC-specific: Triage: 34184 Sjors:2025/12/cool-down
	# Needs review/work: 34213 brunoerg/2026-01-net-anchors-networkactive
	34224 fix_init_int_ec-27					fea22c4cc5d
	34235 fix_miniminer_feeassert_pr34235-26	c156f53033d
	34252 doc_bips_add433-28					f0f7762d376
	-     qt_scope_bringToFront_workaround-28	f8c1921475a
		# Related to gui#914 hebasto-g/251121-wayland
	# Needs review: g915 -  # Defer transaction signing until user clicks Send
	# Redundant with gui#677 (which fixes more): g920  -  # Set peer version and subversion to N/A when not available or detecting
	# Redundant with gui#815 (which fixes more): Needs review: g922  -  # gui: fix transactions disable problem
	34293 fix_vermsg_missing_comma-29+knots		58cde3c7531	last=ffd09f8a0d0 fix_vermsg_missing_comma
	34272 fix_psbt_bounds_assert_pr34272-25		a4e1877fddb
	# Needs followup work? 34281 maflcko/2601-build-fix-remove
		# 30.x backport in #34283
		# + #34413 (see also issue #34414)
		# + #34468 ?
	34282 qafix_win_log_skips_pr34282-24		2147d3e2fea
	# Duplicate of #29678: 34305 fanquake/fix_space_warning_log
		# Consider CeilDiv from #34436
	34328 monotonic_uptime-29					c2a42f7d6d3	last=e67a676df9a !l0rinc/l0rinc/fix-uptime-first-call-zero
		# + #34437
	# Needs review: 34348 -  # lib: call RandFailure() if RDRAND fails
	# Needs review? And/or minimal fix instead? 34349 maflcko/2601-sp-popen-less
	# Triage: Needs review? 34358 mzumsande/202601_importprunedfund_bug
	34369 qa_timeout_factor_netshutdown-29		775dae60e5e
	# Triage: Needs review: 34371 -  # wallet: allow importprunedfunds for spending transactions
	# Needs review: 34379 rkrux/gethdkeys
	# Needs review: 34381 brunoerg/2026-01-scriptnum
	# Needs review: 34393 -  # rpc: Fix off-by-one error in getblockchaininfo help
	# Triage: 34417 maflcko/2601-log-warn-sensitive
	g924  fix_qt_restor_empty_walletname_msg-24	f6af40ef4f2
	# Needs work: 34451 w0xlt/i_34263
		# +#34908 ?
	# Windows-only, doesn't affect us? 34454 avoid_winnt_delete_keyword_conflict-28
	# Triage/needs review: 34456 -  # p2p: assign separate network keys to outbound onion connections
	# Needs review: 34458 sedited/logips_self_discover
	# Needs review: 34467 -  # net: don't perform network activity when networkactive=0
		# OR: 34486 willcl-ark/respect-networkactive
	34470 leveldb_wrkrnd_uninit_debugsize-0.8	bd234a6bd55	last=fad7d86d8d1 maflcko/2602-ci-leveldb-ub
	# Needs review: 34480 danielabrozzoni/issue/26527-dont-backtime-nlocktime-unconf
	# Needs review (and AI removal?): 34530 -  # wallet: guard against negative bump fee discount from mempool race
	# Needs review/concept: 34538 willcl-ark/onlynet-advertisments
TM	34561 docfix_rpcwallet_send_eg_pr34561-23	033685469ee	last=50cf6838e6a
	# Needs review: 34582 maflcko/2602-int-arg
	34597 fix_SetStdinEcho_ub-0.20				7754cfa35a6
	34603 fix_win_IsSymlink-29.3				47d584b32c3	last=b127cde3f4a
	# Needs review? 34614 maflcko/2602-ci-space
	g929  qt_plurals_prg929-21					1fd035c8085	last=746d8cddc19 hebasto-g/260217-translation-plurals
	# Needs review: 34628 ajtowns/202602-mempool-invtosend
	34642 wallet_validqueue_drainforunload-29.3+knots	ae3d304b0bf
		# NOTE: Subtly depends on #30221 (and the PRs bundled with it)
	# Triage: 34655 l0rinc/l0rinc/coins_view_fuzzer_cleanup
	# IPC mining: 34661 ryanofsky/pr/waitmine
	# Needs review: 34678 chriszeng1010/fix-accept-unknown-sockaddr
	34702 docfix_getblock_txfee_condition-22	68e20ff78a2	last=f580cc7e9f2
	# Needs review: 34743 willcl-ark/protect-manual-evictions
	# Only FindQt fix applicable, not worth it? 34754 hebasto/260306-qt6-gcc16
	34767 fix_qt_intro_chain_except				b6c5a5fa30c
	# Triage: 34787 fanquake/ci_test_macos_codesigning
		# NOTE: 31.x backport in #34800
		# NOTE: 30.x backport in #34805
	# Needs concept & review: 34812 w0xlt/fix-33471-cjdns-externalip
	n/a   fix_typos_from_pr33152-29.3			e4d87f04d80
	34870 fix_wallet_bump_fail_crash-29.3		e2a174d3814	last=6072a2a6a1f furszy/2026_feebumper_crash_fix
	# Needs work: 34872 w0xlt/wallet-mixed-input-history-only
	34888 fix_wallet_coinsel_pr34888-25			8cb99ded63c	last=0026b330c4a furszy/2026_wallet_total_amount_bad_comparison
	34893 fix_psbt_merge_proprietary-29			8d7c743b143	last=da769855d0c w0xlt/psbt-proprietary-merge-fix
	# Needs review: 34897 mzumsande/202603_index_sync_dont_commit_ahead
	# Needs review: 34903 HouseOfHufflepuff/wallet-importdescriptors-validate-before-rescan
	# Needs review: 34916 Sjors/2026/03/manpages-locale
	# Needs review: 34931 furszy/2026_utxo_deser_error_divergence OR 34132?
	34937 fix_rlim_infinity-29+knots			7c5b9cf04a5	last=735b25519aa Sjors/2026/03/file-descriptor-limit
		# Held back 101de678a8e...735b25519aa portability regression
		# Fixed bug to make it more portable instead
	# Needs review (work?): g934 sbddesign-g/fix-151-issues-with-new-create-wallet-dialogue
	34959 bdbro_enforce_levels_sizes-28			0fd6ccf8a31	last=b2de59d486d achow101/bdbro-cycle-detection
		# OR: 34946 instagibbs/2026-03-infinite_migrate
	# Triage: Needs review: 34962 cprkrn/test-feebumper-enormous-cluster
	# Needs review: IPC only: 34978 enirox001/04-26-ipc-maxconnections
	# Needs review: IPC only: 35037 enirox001/04-26-ipcbind-max-connections-draft
	34988 fix_init_fiasco_pr34988-28			ce36e2ac3e8
	# Needs review: 34993 davidgumberg/2026-04-02-notifycan
	# Needs review: 34997 danielabrozzoni/getaddr_feeler
	# Needs review: 35003 furszy/2026_abc_io_exception
	# Needs review: 35017 instagibbs/2026-04-remove_all_consensusscript
	# Triage: Needs careful review: 35026 javierpmateos/fix-bip68-stale-lockpoints-clean
	35168 fix_exclude_pruned_from_unlinked-29	384606de07f
		# Includes test framework addition of create_empty_fork from #32587
	35070 fix_FMWC_ub_pr35070-29				6f7594f0066
	# Needs review: 35071 pinheadmz/reindex-continue
	# Needs review: 35137 GerardoTaboada/wallet/document-maxconf-default
	# Triage: Needs review: 35143 thomasbuilds/fix-btck-handle-self-move-assign
	# Needs review: 35145 ViniciusCestarii/verifydb-cleanup
	-     fix_torcontrol_maxlinelen-29+knots	3b7f973b9fe
		# Includes new tests (only) from #34158
	35087 torcontrol_linelimit-29+knots			c272822b32d	last=9fe5896a446 davidgumberg/2026-04-14-torcontrol-linelimit
	# Needs review: 35092 -  # wallet: bound descriptor update work after high-index detection
	# Needs review: 35100 nervana21/20260416_locktime
	# Needs review: 35115 tony-ku/wallet-34599-abandon-confirmed-descendant
	# OR: 34599 Luquitasjeffrey/issue34599
	35116 socks5_redact_authinfo_log-28			7842d74620e
	35117 i2p_redact_privkey_in_log-22			a31486fcaf5	last=b6c36704428 takeshikurosawaa/i2p-session-create-redaction
	# Needs review? 35166 asafmod/harden-prevector-change-capacity
	# Needs review? 35173 l0rinc/l0rinc/thread-name-truncation
	# Triage: Needs review: Or fix-only? 35177 AgusR7/test/getblockstats-gen-miniwallet
	# Needs review: 35185 shuv-amp/fix-importdesc-timestamp-abort
	# Needs review: 35191 ArtSabintsev/codex/fix-txdb-cursor-malformed-key
	# Needs review & UPnP: 35193 vasild/avoid_internet_traffic_from_init_test
	# Needs review: 35208 l0rinc/l0rinc/headerssync-future-mtp-cap
TM	35209 fix_precomptxdata_lifetime_CVE_2024_52911-27	628bd86cfb5
	# Needs review: 35217 -  # psbt: fix PSBTInput::Merge ignoring sighash_type field
	35227 fix_bdbro_check_lastpage_pr35227-28	7bb4d9ccacc	last=e2b0984f995 l0rinc/l0rinc/check-bdb-last-page-lsn
	# Needs review? 35233 l0rinc/l0rinc/external-signer-skip-canceled-duplicates
	35384 fix_settings_writeerror_handling-27	5bb202df945
	-     fix_qt_sync_pct_truncate-28			f447be0250b	last=a3dac13371c origin-pull-g/935/head
		# Rewrote from gui#935 to avoid floating point rounding at any stage
	-     fix_rpccookieperms_early				13f116a4bee
	-     qt_intro_nojumpy						226638f1c40
	-     restore_guix_ppc64le-28				e3f03d24d38
	-     qt_dialogs_less_modal					b5d00404038
	-     docfix_getorphantxs_vsize				91d6b9501fb
		# Originally bundled in Knots with #30793 rpc_getorphantxs
	-     fix_guix_boost_mirror-29				1b25838101a
	-     fix_qt_startup_unknown_unit			a9364cdbcfa
	-     fix_qt_psbtops_filename_amount		0553d2e1479
	k126  fix_qt_progressbar_fittext			aca8267101a
	k150  fix_rpc_mixed_params_edgecases		081fd967a9c
		# Held back (4d24d60836f) support for positional options + named params (breaks tests)
	# Needs work: k182 proxy input validation fixes
	# Needs work: k228 1440000bytes/fix-corruptwallet-crash
	-     qt_nowalletpage_alerts-23				5b533615a3b
	-     fix_alertnotify_winquoting			94a0788e8d9
	-     torcontrol_avoid_bindany_connect		ad5aefdfaa8
	-     fix_tor_common_bind-29.2				6e48865fb7c
		# Core duplicate: #34892
	# Needs review: k254 privkeyio/cmake-hardening-module
	# Needs work? k237 privkeyio/159-build-checks
	k244  fix_qt_amtfield_infinityevent			498501b2db4
	-     fix_win_exclopen-29.3					51fa55be4f9
	k255  wlt_nonlegacy_change_if_no_leg_spkman	aaa3b884749
	# n/a to Knots: -     depends_libevent_ignore_git_desc
		# Only affects libevent builds when the bitcoin tag has 5 components
	# Needs work: k263  privkeyio/fix-vsize-sigops-datacarrier
	k266  extsigner_sanitychk_fingerprint-26	424782b373f	last=304598b5cc5 privkeyio/fix-external-signer-fingerprint-validation
	k277  fix_qt_ban_expiry_update-28			c1738f8f964	last=87fca974185 Bortlesboat/fix-ban-table-refresh
	# Needs review: k298 param_bounds_checks_202604
	k301 qt_always_show_alerts-27				4467714ff49	last=3437824d39b privkeyio/fix-warnings-no-wallet-tabs
	k303 rm_dnsseed_pt							e99d21febda
	k329 privkeyio/fix-gen-bitcoin-conf-datadir	20b6e1d2e76	last=4f5c53851fa
	k336 qt_locale_datetime_prk336-29+k			89d5548bb19	last=2f53648f1a2 privkeyio/fix-gui-datetime-locale
		# Second commit included later in softwareexpiry
	k339 privkeyio/fix-pie-c-link-flags			13f09b8b505	last=66dc2de6c25
	k344 -										6f6605f2091	last=2b54c093cf1 privkeyio/fix-rpcconsole-wallet-selection-consistency
	k360 privkeyio/fix-checkblockindex-ordering	388d70d31d1	last=ed6fb09bfbc
	k375  dnsseed_tn4_leohaf-28					69b960182c6	last=3e3d59a05ba Retropex/testnet-seed
	#30.xTODO# "Knots feature request: system notification for a txn should show the net wallet balance delta assuming the txn confirms, not whatever it does now that gives me a heart attack every time I use a large-ish UTXO lol" -Jason (currently only the first send of a sendmany is shown) https://github.com/bitcoin-core/gui/issues/853
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
	#30.xTODO# Review security report(s)
	n/a   (delete_release_notes_fragments)
#@29.x-knots-lts-deps
	# No point (dynamic linked): 33952 fanquake/close_out_29977
	-     upd_qt5-29.2							2bd4cbdd1d8
		# 5.15.19 Opensource released: https://lists.qt-project.org/pipermail/announce/2026-May/000626.html
	#29.xTODO# FIXME -     depends_qt5kde
	# Needs review: k231  privkeyio/kwsantiago/qt6-depends-upgrade
		# TODO for 6.x: +#33906 (30.x backport in #33609)
		# With Qt6: 33906 hebasto/251118-patch-win11-plugin
			# 30.x backport in #33609
		# With Qt6: 33918 hebasto/251120-qt-link
	k345 privkeyio/depends-libevent-2.1.13		489d4b0035b	last=0515b85e4f3
	# Needs review: 32655 fanquake/sqlite_3_50_0
	# Needs review: 32665 fanquake/boost_shrink
	-     fix_secp256k1_bugs-29					2ee15e9049c
		# bitcoin-core/secp256k1#1731,1749,1821 (diff-minimised and fix-only)
	# Multiprocess-only: 34825 fanquake/capnp_1_4_0
	# Multiprocess-only: 34952 ryanofsky/pr/subtree-9
		# + #34977 ?
@29.x-knots
# PERFORMANCE:
	33915 qa_getprevrel_retrydownload-28		a951168e6e4
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
	# Needs review: 28400 -  # Make provably unsignable standard P2PK and P2MS outpoints unspendable.
	28430 -										4676f54cf6a	last=42b25bbd939  # opti_merkle_mutation-0.17
	28592 -										97383e5d2e5 last=b81f37031c8  # txrelayrate_14txps-26
		# TODO: Make configurable? Or is that even sane?
	# MSVC: Needs review: 29036 theuni/msvc_fast_byteswap
	# Needs review?? 29159 -  # Update net.h bigger TCP socket using larger buffer
	# Needs review: 29473 -  # optimization: Speed up Base58 encoding by 400% by 64-bit preliminary byte packing
	# Needs review: 29491 fjahr/2024-02-batch-validation-updated
	# Needs review: 29578 brunoerg/2024-03-addrman-getaddr
	29602 opti_IsSpace_pr29602-29+knots			e380e727b1d
	# TODO: Revert #29815 ? (ie, use OS provided optimised timingsafe_bcmp)
	30059 dbfilesize_param-29.1					2974b3df1c0	last=c283a572145 dbfilesize_param
	-     dbfilesize_64-29.1+knots				902c34e8bf8
	# Needs review: 30317 -  # WIP Simplify SipHash
	# Needs review: 30325 -  # optimization: Switch CTxMemPool::CalculateDescendants from set to vector to reduce transaction hash calculations
	# Needs review: 30370 fjahr/2024-07-pr28945
		# Was (never in Knots) #28945
	# Needs review? 30442 paplorinc/paplorinc/siphash
	# Needs review: 30610 sipa/202408_force_sync OR 33680 l0rinc/l0rinc/force-sync
	30611 chainstate_write_hourly-29+knots		0ba345ed2c1	last=e976bd30450 andrewtoth/write-chainstate-every-hour
		# Includes new tests from core#32414
		# TODO: Make interval configurable
	# Needs Knots review & diff-minimise: 30987 davidgumberg/zero_after_free_allocator_change
	# Needs review: 31132 andrewtoth/threaded-inputs
	31144 opti_multibyte_xor-29+knots			a3ccb14e573
	31179 -										34944c5aa0c	last=5d82d92aff7  # opti_rpc_uv_reserve-25
	31645 opti_dbbatchsize_64-29				c09c6c781c8	last=b6f8c48946c l0rinc/l0rinc/utxo-dump-batching
		# Held back 868413340f8...b6f8c48946c (reduce to 32 MiB) for now
		# TODO: Test even higher or incrementing-as-we-flush
	# Needs review: 31682 l0rinc/l0rinc/optimize-CheckBlock-input-duplicate-check
	# Needs Review? 31714 mzumsande/202501_simpler_segwit_check
	# Needs reivew: 31868 l0rinc/lorinc/block-serialization-optimizations
	# Needs review: 31875 l0rinc/l0rinc/sorted-BatchWrite
	# Needs work: 32023 -  # wallet: removed duplicate call to GetDescriptorScriptPubKeyMan
		# +#32475
	# Needs review: 32128 -  # Draft: CCoinMap Experiments
	# Needs review: 32150 murchandamus/2025-03-rewrite-BnB
	32279 opti_script_inline_36b-29				c172b86b4ea	last=d5104cfbaeb l0rinc/l0rinc/prevector-size
	32487 opti_readblock_hash_once-29			abae37af4e6
	-     netproc_check_blockhash				8a8294f4a16
	# Needs review: 32497 opti_merkle_reserves-21							last=39b6c139bd6 l0rinc/l0rinc/pre‑reserve-merkle-leaves-to-max
	# Needs careful review: 32532 l0rinc/l0rinc/short-circuit-known-script-types
	# Needs review: 32645 theStack/202505-fs-use_ftruncate_on_openbsd
		# NOTE: ftruncate does not guarantee allocation normally? and we don't want to truncate!
	# Needs work: 32692 -  # TODO: Dynamic scriptcheck thread count
	# Needs review: 32730 furszy/2025_net_avoid_traversing_block_twice
	# Needs review: 32791 -  # checkqueue: implement a new scriptcheck worker pool with atomic variables
	32827 opti_removeForBlock_empty-28			85d2a2d25e8	last=249889bee6b l0rinc/l0rinc/empty-mempool-IBD
	# Needs work/review: 32885 pstratem/2025-07-05-lockless-isibd
	# Needs review: 33031 achow101/lasthardened-cache-migratewallet
	# Needs Qt5 compat: 33217 rm_xinerama-23									last=e9623be19ad fanquake/drop_xinerama
		# Broken backport to 29.x in #33238
	# Needs review: 33253 ajtowns/202508-cache-friendly-compactblock
	#29.xTODO# 33264 kevkevinpal/reduceScopeOfGetBlockTemplateLock
	# Needs work? 33299 wallet_sqlite_version_once-21						last=862faf3fa7a mzumsande/2025_wallet_log_less
	#29.xTODO# After 29.2 (to avoid rebuilding Qt): 33304 fanquake/strip_qt_bins
	# Needs review: 33306 fjahr/2025-09-csi-compaction
	# Conflicts with #18014? Needs review: 33325 Raimo33/siphash-write-chunked
	# Needs review: 33328 -  # Mapping for Lockedpool
	33332 opti_arith_uint256_trivialcopy-28		2dff498d8ed
	33334 opti_blkidx_comparator-26+knots		be882526bc6	last=80ac0467ef4 Raimo33/index-work-comparator-branchless
	33410 opti_coinstats_nocopy_pr33410-26		473a436f3ae	last=85d058dc537  # coinstats: avoid unnecessary Coin copy in ApplyHash
		# Real last=5a56203f4e4 (branch messed up by author)
	# Needs review? 33602 l0rinc/l0rinc/BatchWrite-lookup-optimization
	# Needs review: 33637 l0rinc/l0rinc/block_index_comparators
	# Needs review: 33645 Raimo33/optimize-tx-policy-verification
	33738 opti_cmpctblocks_nolog_skip_hash-29	7997bf4c707	last=969c840db52 l0rinc/l0rinc/debug-log-serialization
		# Very partial
	# Needs review: 33757 l0rinc/l0rinc/solutions-vector-optional
	# Needs concept (even if merged) & review: 33817 l0rinc/l0rinc/bip30-bloom-filter-removal
	# Needs careful review: 34004 -  # Implementation of SwiftSync
	34025 cache_time_and_arg_pr34025-29			6ada3d4bda5
	# Needs review: 34054 sedited/txdownloadman_ibd_check
	# Needs review: 34083 theuni/chacha20-vectorized-initial
	34253 lockless_isibd-26+knots				baa1453b663	last=557b41a38cc l0rinc/l0rinc/cache-ibd-status
		# NOTE: diff-minimised, and did not backport refactor commits
		# NOTE: various libbitcoinkernel changes needed, if libbitcoinkernel features (#30595 in particular) are backported
	# Needs review: 34400 -  # wallet: parallel fast rescan (approx 5x speed up with 16 threads)
		# + #34667 ? +#34907 ?
	# Needs review: 34405 -  # wallet: skip APS when no partial spend exists
	# Needs review: 34424 -  # [RFC] CChain Concurrency Improvement (Base + Tail Architecture)
	# Needs review & worth-it evaluation: 34483 maflcko/2602-span-reader
	# Needs review: 34489 furszy/2026_index_batch_processing
	34612 leveldb_slim_pr34612-29				4a34c22b1a6	last=3feabb203a6 fanquake/unused_historgram
	# Needs review? 34613 -  # replace manual byte copies
	# Just removes a Guix dep: 34627 fanquake/replace_sponge
		# + #34944 ?
	# ----- DBCACHE DEFAULT/WARNING -----
	33333 dbcache_too_high_warning-29.3+knots	1c4db2fd6f1
		# + #33435
	34692 dbcache_1GiB-29.3+knots				f6e558d7794	last=4ae9a10ada9 andrewtoth/bump_dbcache
		# Excluded doc update & release notes
	35097 byte_units_64bit_GiB-29.3+knots		a6f64450575
		# Partial; + #34435 (partial)
		# Fixed missing header
	34641 dbcache_dynamic-29.3+knots			fe12d13851f
		# + #34106 copyright notice + misc fixups
		# Omitted refactors, doc changes & release notes
		# NOTE: last= removed because upstream branch destroyed
	# Needs review: 35200 l0rinc/l0rinc/smooth-dbcache-warnings
	# After working mempressure: k279  privkeyio/feature-autosize-dbcache
	# TODO: cgroup-awareness as a default limit? (see also #34762)
	# ----- END OF DBCACHE DEFAULT/WARNING -----
	# Needs review: 34656 alexanderwiederin/blockmap-chain-concurrency
	# Needs review: 34794 w0xlt/rest-cache-control-headers
	# Needs concept & review: 34932 w0xlt/cmpctblock-shortid-collision-recovery
	# Needs review: 35041 brunoerg/2026-04-descriptor
	# TODO: 35128 l0rinc/l0rinc/dbwrapper-key-spanreader
	# TODO: 35156 l0rinc/l0rinc/ScopedDataStreamUsage
	35195 cache_outpoint_sethash-27				f88f89b5a40	last=16e77fdf132 l0rinc/l0rinc/noexcept-false
	35197 lld_icf_safe-28						451b87a82c3	last=24ad7419dea fanquake/lld_icf_safe
		# Held back 09de5363d36...24ad7419dea: Moved to CMakeLists (applies to non-guix builds) and attempts --icf=safe_thunks (requires LLVM 20+)
		# When bumping to LLVM 20+, upgrade this to safe_thunks too
	# Needs review: 35215 l0rinc/l0rinc/siphash-jumbo
	35825 privkeyio/net-addconnection-count-guard-core	303426c028a	last=ca7c1456f56
	# Needs review: k278  privkeyio/feature-runtime-scriptcheck-calibration
	k287  privkeyio/uncap-scriptcheck-threads	47dcc421a02	last=f23f08cb01f
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
	#-     rm_kernel_lib							84b7c6adf43
		# TODO: Support libbitcoinkernel (see 9da0bc3eba7 history for incomplete attempt)
			# When restoring libbitcoinkernel support, adjust libbitcoinconsensus reverts to make it interact with --with-libs (see 7ad32d39d76)
	-     rm_multiprocess						636e7dd3760
		# TODO: Support libmultiprocess
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
	18479 rpc_sign_show_fees					ec846597d8e	last=47b2ba29df2 !origin-pull/12911/head
		# Dropped rel notes file
		# NOTE: Originally #12911
		#29.xTODO# FIXME: "feerate" fails to account for sigops (see 21d85b5c0e); most of a fix in stash 835c2d3afba
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
	15836 fee_histogram+pr15836_api				5a205e5f98e	last=b94292a7cb jonasschnelli/2019/04/feeinfo
	(CHECK-LAST)	last=c5e53d0d21f origin-pull/21422/head
		# NOTE: Now rebased on top of #21422 (but keeping API from #15836 & prior Knots)
		# NOTE: Added extra tests for compatibility with old Knots
		# TODO: Replace with #21422 API ? (or not, since it's been abandoned...)
		# TODO: Drop ec2326304e0 since it's not needed with changes made in 998c34d27e7
	# TODO: 22891 prayank23/mempool-getinfo
	# Totally broken: g108 jonas-g/2020/03/mempool_graph									last=42b451ebf1e
		# TODO: Check gui#320 for usability
		# TODO: https://twitter.com/RandyMcMillan/status/1490107008443457538?t=Qc4LO63rRuWxErtRel06EQ&s=19
		# 			aka 4613c88c91f4f3846aa62c929ad73d1a3e6ac70e
	22693 getaddressinfo_txids					a7027c55945
	g562  wallet_warn_reuse_gui					ed5350bc20c
		# NOTE: Was #15987
	# Needs review: 16066 promag:2019-05-ibd-avoid-mempool-estimator
	# Needs review: 16145 promag:2019-06-prevent-idle-sleep-ibd
	# needs completion: 15876 [rpc] signer send and fee bump convenience methods
	# Needs work? 16698 [WIP] Mempool: rework rebroadcast logic to improve privacy
	# Needs careful review: 17060 martinus:2019-09-more-compact-Coin
	18972 neutrino_whitelist-mini				bdad3d789c9	last=a0d0807abc2 neutrino_whitelist
		# NOTE: Diff-minimised
	# Needs work/review AND CONCEPT ACK: 17950 emilengler:2020-01-password-strength-checker
	-     qt_openuri_pastebtn_shortcut-23		afd93b0fd03
		# NOTE: Used to be part of gui#319 (formerly #17955)
	# Needs work/review: 17978 -  # gui: walletcontroller showProgressDialogue functional progressBar
	18014 siphash_optimise_pr18014-27+knots		ac57a697f7f	last=409c2e34522 elichai/2020-01-siphash
		# NOTE: Dropped benchmarks & diff-minimised
	# Needs work: 18421 -  # Periodically update DNS caches for better privacy of non-reachable nodes
	# Needs work? 18611 -  # cli: show default values in config args log
	24202 rpc_dumptxoutset_hr-29+knots			31552ad8980	last=1053636ddd9
	(CHECK-LAST)	last=65d0697fe34 origin-pull/18689/head
		# Diff-minimised
		# NOTE: Was #18689
		# FIXME: blockhash+header line is weird https://github.com/bitcoin/bitcoin/pull/24202#discussion_r801191486
	# Needs concept consideration: 18830 brakmic:getrpcinfo (security: potentially can decloak/aid in bypassing proxies?)
	# Needs review: 18849 jb55:zeroalloc
	19242 uaappend								203f693e3cc
		# ALSO: Fixes uacomment test, promotes uacomment to non-debug, and includes -uaspoof
	# Needs review: 19271 andrewtoth:warm-coinscache
	# needs review: 19443 nextpagepointer & list ordering options for listtransactions
		# w/ 22807 ?
	19463 prune_locks							cb7e6bfd35f
		# Consider accepting #34534's changes or rebasing on it
	# Needs review & deo: 19792 -  # rpc: Add dumpcoinstats
	# Needs work: g27   # top to bottom UI layout
		# NOTE: Included in Android fork below?
	# Needs concept ACK: 19635 -ephemeraltoronion
	# Wait for Core? Or rework to use independent db... 19790 blkindex_scriptschecked_flag
	19873 mempressure-29+knots					fa5af6b9b84	last=5b43cc77824 mempressure
	(CHECK-LAST)	last=922bc46001e origin-pull-k/295/head
		# BROKEN: Linux available memory detection no longer correct; we have different kinds of flushes now; and we need to ensure the OS can actually reclaim the freed memory
		# + knots#295
		# TODO: knots#219
		# TODO: LevelDB flushing causes burst of memory usage; consider that here; see #31645
	# Needs review/testing: - maxmem_coins_cache
		# TODO: Some way to override... see #26471 discussion
	# Needs work: g86   hebasto-g/200902-tor
	# Needs work: 20172 hebasto/201016-tor
	g291  gui_trafficgraph_vert-0.21			50c1e43be59	last=500841e49d6  # Enlarge Network Traffic Graph
		# WAS gui#90
		# Removed dialog size change
		# didn't bother with 1f373f93a60...500841e49d6 only changing widget names
	# TODO: Can we support addnode RPC w/ explicit proxy for the one connection?
	# Needs review and diff-minimisation: 20273 jonasschnelli/2020/10/client_rpc_nested
	# Needs review: 20331 -  # allow -loadblock blocks to be unsorted
	# Needs work/concept/review: 20361 -  # load wallets from entropy (as BIP39)
	20391 rpc_setfeerate-28+knots				9aa118ee195	last=1002e2d0d7f jonatack/setfeerate
	# OR (evaluate): 31278 -  # wallet, rpc: Settxfeerate
		# NOTE: Minimised tests to only add new ones
		# NOTE: Held back refactoring & unrelated changes
		# TODO? Reduce internal changes and move to Knots compat??
	20407 rpcauthfile-29+knots					4f95c923a3b	last=ff5d7fa1e4c promag/2020-11-rpcauthfile
		# NOTE: fixed bugs, added multi-line support, and added tests
	# Needs polishing: g135  -  # peers-tab: cleaner presentation - more info - functionality improvements
	# Needs polishing?? 35198 arejula27/truncate_header_sync_percentage
	g149  intro_assumevalid						5ff05136c61	last=cf940f0e5f5
		# NOTE: Added compatibility for older Qt versions
	# Needs review: 20652 -  # Designer fees when coin control is enabled
	20702 rpc_getblocklocations					ef0e247cd61	last=9b03c654eb3
		# NOTE: Fixed +x on test/functional/rpc_getblocklocations.py
		# NOTE: Added necessary(?) cs_main locking
		# NOTE: Fixed typo in RPC example doc
	# Needs BIP final(?): 20726 sdaftuar:2020-12-negotiate-block-relay
	g363  qt_peers_directionarrow-25+knots		0417b01d9c2	last=727a2f83cca qt_peers_directionarrow
		# WHEN REMOVING/MERGED UPSTREAM: Table column widths change removed in upstream PR; preserve it for Knots somewhere
		# WHEN REMOVING/MERGED UPSTREAM: Reverted 51708c4516c (from gui#543) - also preserve for Knots
		# TODO: Should align the direction column on the right side, but Qt ignores alignment for icons :/
	# Needs work: 15129 remove_watch_only_address-22			423fd4425f4	last=b8eb5880693 benthecarman/remove_watch_only_address
		# Was included in 0.21.1 broken(!)
		# See https://github.com/bitcoin/bitcoin/pull/15129#discussion_r733010724
	21928 rpc_hww_toggle-25						6bbbaca4bfb	last=1af20831806 Sjors/2021/05/hww-toggle
	# Needs work? 17355 -  # gui: grey out used address in address book
		# TODO: Code review & make sure no wallet db changes (if it does, store in RAM for Knots for now?)
	# TODO: 21283 achow101/psbt2
		# TODO: diff-minimise??
	21260 rpcwallet_tx_in_mempool-29+knots		370bba9c7ce	last=46bf0b7b5d8
		# Includes squashed fixes for RPC doc
	# Needs API work: 21284 -  # rpc: add the add_inputs option to bumpfee/psbtbumpfee
		# NOTE: Ensure default is actually true
	# Needs work: 21312 -  # wallet: remove lock during `listaddressgroupings`
	# Included in gui#662 above: g368  bugfix_gui_restored_columns_stretch	3b888b39d64
	g230  gui_backup_formats					3d4624608e7
	# Needs Concept ACK & review: 21515 naumenkogs:2021-03-erlay
		# +27797 ?
	# Needs review: 21618 rebroad:MinRelayFeeReductionChanges
	21780 rpc_maxmempool						d5850c3fb9f	last=040b280c661 rebroad/MaxMempoolRPC
		# + bugfix and applying limit immediately
	# Needs review: 21827 rebroad/SplashLoadBlockProgress
	# Needs review: 21841 rebroad/SteadierFeefilter
	22072 autoreindex-29+knots					bc1d2a1f8c9	last=602f4da9178
	(CHECK-LAST)	last=6d7052863a5 origin-pull/26674/head
		# TODO: Migrate to #26674 (basically identical logic as of 6d7052863a5) ?
	# Not useful: g358  jarolrod-g/themedlabel-forms
	g307  gui_peers_rowcolouropt				a3683952b05	last=fdf80937d1c hebasto-g/210501-stripes
		# Dropped formatting changes and avoided conflict with g216(optional_font)
	# TODO: Change to have both? g305 rebroad-g/SendRecvSpeed-gui
	# Needs work? 34438 w0xlt/gethdkey
		# WAS: Too many TODOs: 22341 Sjors/2021/06/getxpub
			# NOTE: Might require #28192
	# Needs work: 22350 -  # Log rotation
	22372 multinotify							29eaa35a024
	24963 rpc_walletprocesspsbt_options-26		f6e039f0b53	last=40143bafb52 rpc_walletprocesspsbt_options
		# Diff-minimised (and uses merge for rpcarg_type_per_name)
		# Held back f43f992b731...40143bafb52:
			#* 40143bafb52 QA: rpc_psbt: Test that the wrong type cannot be given to named params
			#* 7cd0315bc40 RPC: Strictly enforce the type of parameters passed by name
	-     rpc_descriptorprocesspsbt_opts		789b53ece09
	# Needs review: 22563 vasild/addrman_per_group_bucketing
	# Needs review: 25621 -  # rpc/wallet: Add details and duplicate section for simulaterawtransaction
	# Needs work: 22775 -  # rpc: Add option to list transactions from oldest to newest in listtransactions RPC command
	# Needs review: 22919 -  # fees: skip pointless fee parameter calculation during IBD
	# Needs work: 23019 -  # rpc, wallet: Add listaddresses RPC
	# Needs review: 23035 jonatack:getnodeaddresses-tried-and-reference_count
	# Needs review: g410  benthecarman-g/uppercase-uri
	23362 importfromcoldcard					e1ee3583cd1	last=8076f8d4c2a hebasto/211025-cc
		# THIS WAS BROKEN (affects MakeDatabase), NOW OMITTED: Instead of changing behaviour of wallettool's WalletCreate, just do the two lines inline (see diff-end of d70ada16a69)
		# Added experimental warning
	23387 rpc_savefeeestimates-29+knots			02273f38928	last=d5b41e6b2ed greenaddress/dump_fee_estimates  # savefeeestimates
		# NOTE: Carries lock annotation fix aa096ebfb06 (FlushFeeEstimates lock on m_cs_fee_estimator)
	# Needs fixes: g457 shaavan:peer-table-splitter
	# Needs work/review: 23475 -  # wallet: add config to prioritize a solution that doesn't create change in coin selection
	# Needs concept + review + BIP: 23531 prusnak/yggdrasil
	# Needs review/deps: 23544 Sjors/2021/11/no_descriptors
	# Needs review: 23624 -  # zmq: add rawmempooltx publisher
	g473  rebroad-g/NonLinearTraffic			1e6bb009f0c	last=ad431ff5d18
		# TODO? change to logarithmic scale? 8398d247f4e
	# Needs work: g484 rebroad-g/RetainNetworkGraphOnIntervalChange
	g492  qt_traffic_tooltip					1a23a0c894e	last=6c139ebf710 rebroad-g/NetworkGraphTooltip
		# Left off top commit which breaks behaviour, fixed some nits
		# Rebased on top of gui#473
	# Needs work: g866 rebroad-g/trafficgraphwidget-rebased
	# Needs work: k104 rebroad-g/ more traffic graph stuff
	g820  qt_fontsel_qrcodes-27+knots			30c1615e36a	last=b14c9d0572e qt_fontsel_qrcodes
	# TODO: qt_fontsel_console
	# Needs review: 24007 -  # [mempool] allow tx replacement by smaller witness
	-     verifymsg_bip137_and_electrum			11ebec41d36
		# NOTE: Fully reverts gui#819 in anticipation of #24058
	24058 bip322-29+knots						f0d9c169364	last=29b28d07fa9 kallewoof/202201-bip322
		# gui#819 fully reverted above in anticipation of this
	#30.xTODO# signmessagewithprivkey updates for BIP137+Electrum+BIP322
	# Needs work: 24123 fanquake/mbranch_protection_aarch64_linux
	# Needs review: 24128 -  # wallet: BIP 326 sequence based anti-fee-snipe for taproot inputs
	24162 rpc_deriveaddr_wo_checksum-29			3a19e3c13fe	last=97a69e232be
		# +RPC doc fix
	# Needs work/diff-minimisation: 24170 -  # p2p, rpc: Manual block-relay-only connections with addnode
	# Needs work: g533  -  # gui: add more detailed address error message
		# TODO: Maybe a button inside the lineedit to display the error message?
	# OR: Needs work? g560 w0xlt-g/3_error_message_addr
	# Needs review: 24539   # Add a "tx output spender" index (txospender)
		# + #34635 ? + #34653 ? + #34747 ? + #34749 ?
		# Check out #34637
	# Needs conceptual review: 34636 svanstaa/improve-index-cache-allocation
	# Needs review: 33904 kevkevinpal/feat/rest-gettxspendingprevout
	# TODO? BIP 179 (tho... Lightning) - upstream first to get translations?
	# Needs work: 24897 w0xlt/silent_payment_021
	# Needs work: 24950 -  # Add config option to set max debug log size
	# Needs work: 24952 -  # rpc: Add sqlite format option for dumptxoutset
	# Concept NACK? 25026 -  # rpc: Make pruneblockchain fetch old blocks if height is lower than pruned height
	# TODO? Needs careful review? -     stratum_server	last=36bbfbc0e7b tradecraft/bitcoin-merge-mining-23
		# Caution: Has a bug per call w/ maaku ???
	25183 rpc_fundraw_segwitonly				a425b3398cb	last=9e7fd5c0fe3
	(CHECK-LAST)	last=edf8e63393b origin-pull-k/293/head
		# Currently just an old version for Knots 23.0 compatibility (held back 1c5cfd84b3d...9e7fd5c0fe3)
		# Fixed tests with inspiration from 9e7fd5c0fe3
		# + knots#293
		# TODO: update without breaking compatibility? (new code looks buggy tho - needs rewrite?) (also, filtering by "input type" doesn't really make sense, though segwit filtering does)
	# Needs concept: 25261 -  # rpc: fetch multiple headers in getblockheader()
		# Was: Needs API review: 23330 JeremyRubin/header-fetch
	# Needs review: 34299 -  # wallet: re-activate "AmountWithFeeExceedsBalance" error
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
	#30.xTODO# sendrawtransaction to a specific node bypassing mempool
		# See https://github.com/bitcoinknots/bitcoin/issues/50
	# Needs review: 26174 w0xlt/list_address_book
	-     whitelist_outgoing_auto				13eb63ae6be
	# Needs work: 26441 brunoerg/2022-10-whitelist-rpc
		# CAUTION: neutrino whitelisting interaction
	27446 benthecarman/configure-signet-blockitme	813e1cc9d5f	last=d8434da3c14
	# Needs work: 26495 -  # contrib: Speed up systemd boot
	# TODO: Simplify [initial] wallet creation
		# See: https://twitter.com/susewang/status/1591115373465972737?t=FGNyW1PSmjpT0u-lR7lNiw&s=19
	26576 rpc_disconnectnode_subnet				bef7ec23e7d	last=23f4c2cb452 brunoerg/2022-11-disconnectnode-subnet
		# Refactored tests (to be more deterministic) and added support for disconnecting a single IP without subnet specified
	# Waiting for Core or BIP: 26626 achow101/desc-key-list-expr
	# Waiting for #26626: 26627 achow101/migrate-nonhd-key-list
	# Needs work: 26938 brunoerg/2023-01-avoid-as
	# Needs review (and opt-in?): 26988 -  # cli: rework -addrinfo cli to use addresses which aren’t filtered for quality/recency
	27034 rpc_importaddr_for_descwallet-27+k	67193a41ee4	last=be3ae51ece8 furszy/2022_rpc_importaddress_descriptors_compatible
		# Diff-minimised & tweaked to avoid breaking #23362
	27052 rpc_getpeerinfo_lastblockann-28		bb3b47562c3	last=13ce46ba1a7 LarryRuane/2023-02-getpeerinfo
		# Avoided changing internal data structures
		# Held back test removal 036a87b8a99...136eed4a13c
		# Held back type changes 252a6e72754...13ce46ba1a7
	27216 rpc_getaddressinfo_isactive			27f51c23273	last=85f83339dda pinheadmz/used-addr-ui
	# Needs work: 27260 -  # Enhanced error messages for invalid network prefix during address parsing.
	27351 codex32-29+knots						4aa0553a97d	last=91771366a3d apoelstra/2023-03--codex32
		# + knots#267
		# See #32652 if #29136 is merged
		# Diff-minimised, doc bug fixed & tweaked to avoid breaking #23362
	# Needs concept & review: 33043 w0xlt/codex32
	# Needs work: 27409 ryanofsky/pr/1data
	# Needs review: g692 -  # Debug Console implementation of generate method
	# Needs work: g700 achow101-g/bumpfee-choose-reduce-output
		# Careful, could end up paying "added change" to a destination -.-
	# Needs concept/review: g723 pinheadmz-g/used-addr-ui-gui
	27600 p2p_forceinbound-28+knots				8e2a6941b85	last=8c2026848da pinheadmz/whitebind-evict
		# Reverted forceinbound limit anti-feature (& rel notes)
		# Moved ForceInbound permission flag to bit 10 to avoid conflict with neutrino whitelisting
	# Needs work: 27638 -  # rpc: show P2(W)SH redeemScript in getrawtransaction
	27770 rpc_getblockfileinfo-28+knots			cc499f5d970	last=5090771f326 furszy/2023_rpc_getblockfileinfo
	(CHECK-LAST)	last=1543c870273 origin-pull-k/294/head
		# + knots#294
	#30.xTODO# Needs review & BIP finality: 28201 josibake/implement-bip352-sending
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
	29016 rpc_listmempooltxs-29+knots			72906d1a792	last=07008477b81 niftynei/nifty/listmempoolentry
		# Added bugfix to handle parse error in REST code
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
	-     manpages_seealso_notself				8d996e73684
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
	# Triage: 34141 achow101/musig-miniscript
	# Needs review: 34697 shuv-amp/fix-musig-descriptor-dupkey
	# Needs review: 35154 trail-of-forks/security/fix-signmusig2-psbt-assert
	# Needs review: 35155 trail-of-forks/security/fix-setmusig2-secnonce-assert
	# ----- END OF MUSIG2 -----
	#30.xTODO# 29954 rpc_getmpinfo_policy_pr29954-28+knots				last=d165ac8779b kristapsk/getmempoolinfo-permitbaremultisig-maxdatacarriersize
		# Or maybe this is unnecessary with a get/set policy RPC method?
	#30.xTODO# -     rpc_getmpinfo_policy_coreetc-28+knots
	# Needs review: 29959 laanwj/2024-04-qtsowrap-wayland (needs also #29923)
	# Needs review: 30080 -  # wallet: add coin selection parameter add_excess_to_recipient_position for changeless txs with excess that would be added to fees
	# Needs review & Core release (wallet format): 30243 -  # Tr partial descriptors
	#30.xTODO# Needs concept? 30341 willcl-ark/psbt-strip-derivs-combine
	# Needs concept? 30381 willcl-ark/addnode-failure
	# Needs review? g832 -  # Improve user dialog when signing multisig psbts
	# Needs review/optional? 30572 ariard/reject-unsolicited-txn
		# Was #21224
	#29.xTODO# 30595(+34986) + 33791 + 33796 + 33822 + 33825 + 34401 + 34982 + 35187 + 35189?  libbitcoinkernel C API
	30635 rpc_waitfornewblock_tip_param-29+k	8dcac23db39	last=c6e2c31c551 Sjors/2024/08/waitforblock
	# Needs review: 30685 hebasto/240820-control-flow
	30713 -										a8026617b8b	last=5b2d0216d87  # rpc_scanblocks_status_results-28
	#30.xTODO# Mitigate #30717 breaking compatibility with no-longer-debug opts
	# Needs work? 30727 jonatack/2024-08-add-address-type-to-getaddressinfo
	30860 bashcomp_bcli_generate-29				ae8b8393d49	last=abf6ad42bdb BrandonOdiwuor/bash-completion
		# Bugfix + Left off re-generation until later
	k190  feat_zsh_completion-29				df10fbf2ec6	last=e3f6d308a97  # Add zsh completion script generation support
		# NOTE: Core alternatives in #33402 and #34906
	# Needs work: k199 mstampfer/cmake-zsh-completion-only
	# Needs Knots-specific work: 34721 willcl-ark/cmake-shell-completions
	30886 rpc_descrprocesspsbt_prevtxs-28+knots	f33ee01de20	last=87ceb610a72 instagibbs/2024-09-updateutxo_psbt
		# Avoided doc-code move
		# Alternative: Needs review? 34992 bittoby/rpc-utxoupdatepsbt-add-prev-txs
	# Needs work: 31086 dnsseed_cdecker-28								last=5b823920836 cdecker/202442-re-add-bitcoinstats-seed
	# Needs work? 31252 rpc_TxToUniv_witScript-28								last=4e128d4f9b2
		# Alternative: 31256 naiyoma/feature/rpc-show-redeemscript-in-P2WSH-and-P2SH
	# Needs concept ACK: 31353 jonatack/2024-11-total-wallet-balance
	31560 rpc_dumptxoutset_fifo-29+knots		b148e2be270	last=b19caeea098 theStack/202412-dumptxoutset-allow_write_to_named_pipe
		# Held back 509d871fc00...b19caeea098 formatting changes
		# Only the FIFO capability, left out the bundled scripts
	# Needs work? 31668 -  # Added rescan option for import descriptors
	31672 peer_cpu_load-29+knots				c0a1fdfcb85	last=52f1efc06af vasild/peer_cpu_load
	31845 pruneduringinit-29+knots				896e83f99f8	last=d4a3abf6d43 pruneduringinit
		# TODO: + knots#158 ?
	31886 netinfo_local_svcs-29+knots			b862719e9fc	last=721a051320f jonatack/2025-02-netinfo-services
	# Needs work: 31936 -  # rpc: Support v3 raw transactions creation
	31953 bumpfee_full_rbf-29+knots				efa61638db7	last=fa86190e6ed maflcko/2502-fullrbf-follow-up
		# Was: 26454 petertodd/2022-feebump-without-optin
		# NOTE: Added warning to GUI and made RPC behaviour change optional
	32200 socks_tor_error_codes-0.18			254dc2528b2
	# Needs work? 32297 ryanofsky/pr/ipc-cli
	32423 hash_rpcuserpass-29+knots				522b43cf913	last=e49a7274a21 laanwj/2025-05-remove-rpcpassword-deprecation
		# Left out refactoring
	32425 proxy_per_net-29						df225e467d1	last=e98c51fcce9 vasild/proxy_per_network
		# Left out doc updates/reformatting
	32429 doc_rpc_keypoolrefill_pr32429-23		fcdb293f36b
	# Needs work: 32468 -  # rpc: generatetomany
	# Needs concept & review: 32471 -  # Fix listdescriptors true fails with 'Can't get descriptor string' in non-watch-only descriptor wallet
	# Needs review; 32489 achow101/export-watchonly-wallet
	# Needs review: g872 achow101-g/export-watchonly-wallet-gui
	# Needs work: g870 -  # Expose AssumeUTXO Load Snapshot Functionality To The GUI
	# Needs concept & work: 32501 BrandonOdiwuor/removeprunedfunds-array
	# Needs review: 32517 pinheadmz/wallet-gettransaction-ischange
	32540 rest_spenttxouts-26					4c159eac8c7
		# +32842
	# Needs concept review: 32541 -  # index: store per-block transaction locations for efficient lookups
	# Needs review: 32638 l0rinc/l0rinc/read-block-hash-check
	# WIP: 32741 rpc_getpeerinfo_nodeid-28							last=9393b33325e
		# OR #32972 ?
	# TODO: Review ParseHDKeypath change: Part of: 32784 Sjors/2025/06/gethdkey
	32844 rpc_gettxoutproof_segwit-27+knots		d164d77ce1f	last=23edd3db4f1 rpc_gettxoutproof_segwit
	# WIP: 32857 Sjors/2025/07/no_script_path
	# Needs review: 32896 ishaanam/wallet_v3_txs
		# +#33528 glozow/2025-09-send (30.x backport in #33997)
		# +#34238 instagibbs/2026-01-trucness_reorg
	33004 def_natpmp_true-29					8743053de01
	# Needs review & wallet format release: 33008 Sjors/2025/07/bip388-register
	#30.xTODO# Revert #33069 (wallet: Add Support for BIP-353 DNS-Based Bitcoin Address via External Resolver) ?
	# Needs concept: g882 -  # qt: add shift key modifier to clear command history when clearing the console
	# Needs review: 33191 ajtowns/202508-sendtemplate1
	33230 rpc_cli_hashorheight-29				126ecc72708	last=df67bb6fd84 achow101/cli-strong-or-json
		# Left off test changes
	# Needs work? 33259 rpc_getblockchaininfo_bgvalidation-26				last=c1f545248ea  # rpc, logging: add backgroundvalidation to getblockchaininfo
	#30.xTODO# 33290 Sjors/2025/08/missing_capnp
	# Needs work: 33324 l0rinc/l0rinc/reobfuscate-blocks
	# Needs review: 33336 l0rinc/l0rinc/log-initial-signature-verification-state
	# Needs work? 33353 l0rinc/l0rinc/show-reindex-progress
	# Needs concept & review: 33392 -  # wallet/rpc: add scan_utxoset option to getbalance(s) to verify wallet balance accuracy
	33414 tor_pow-29+knots						869225fcf9b
		# + #34158 top 2 commits (see fix_torcontrol_maxlinelen-29+knots earlier)
	# Needs review: 33448 ajtowns/202508-reportinvtosend
	# Needs work (new doc only applies to guix bins) & backport: 33451 hebasto/250921-install-docs
	# Don't care about signet: g896 -  # rpcconsole: display signet challenge
	# Needs work: 33507 rpc_sendrawtxtopeer-25							last=fca25c57efd
	# Needs concept & compat: 33531 w0xlt/multiple_utxos3
	# Needs review: 33540 pablomartin4btc/argsman-GNU-style-command-line-option-parsing
	# Needs work: g898 apogio-g/feature-utxo-viewer
	# Needs review/concept: 33631 fjahr/202510-asmap-arg-split OR 33632 fjahr/202510-asmap-arg-improve
	# Needs concept EVEN IF MERGED: 33657 -  # rest: allow reading partial block data from storage
		# +#34074
	# Needs concept & review: 33671 ajtowns/202510-wallet-unconf-bal
	# Needs concept & review: g911  ajtowns-g/202511-wallet-unconf-bal-gui
	# Needs review: 33752 -  # rest: Query predecessor headers using negative count param
	# Needs review: g902 prusnak-g/desktop-file
	# Needs work: g909 waketraindev-g/2025-11-gui-comment-sensitive-commands
	# Needs work: g925 w0xlt-g/hide_conflicted
	# Needs work: 34512 Sjors/2026/02/getblockfields
	# Needs review: 34606 l0rinc/l0rinc/common-warn-high-swap-usage
	# Needs concept & review: 34640 davidgumberg/2026-02-20-send-minfee-msg
		# last=b77555c8fba backported as 891343f1c57
	# Needs review: 34683 willcl-ark/json-rpc-schema
	# Not worth it? 34713 hebasto/260302-qt-mkdir
		# NOTE: 30.x backport in #34689
	# Not worth it? 34759 theStack/202603-walletdb-clear_out_secret_data
	# Needs review: 34765 overcookedpanda/fix-analyzepsbt-invalid-sig
	34776 guix_clean_confirm-22					bb4a322ad75	last=2724c392080 !origin-pull/34800/head^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	# Needs concept & review: 34829 chriszeng1010/rpc-getrawtransaction-wtxid
	# Needs concept & review: 34933 davidgumberg/2026-03-26-dont-disconnect-unknown-block-hash-cfilters
	# Needs concept & review: 35004 HowHsu/usdt-txgraph-tracing-v2
	# Needs review: 35006 torkelrogstad/2026-04-05-request-id
	# Needs concept & review: 35009 alfonsoromanz/wallet-listtransactions-include-change
	35076 doc_pruning_impact_pr35076-24			8e7517d94b7	last=51ee8ca1683
	# Needs work: 35113 optout21/block-dl
	# Needs BIP & review: 35221 ajtowns/202604-bip434-support
	# Needs concept & review: 35224 kevkevinpal/importDescriptorsPrintoutRequestOnFailure
	-     qt_createunsigned_use_psbtops			1d3a2571a6e
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
	8751  sort-multisigs-28+knots				11c5624bd74	last=e11cb50a09  # multisig sorting
		# held back 50e2ff58f2..e11cb50a09 which turned options into a boolean directly
	22016 rpc_gbci_period_start					8d898f76aa5	last=1898b9be12c Sjors/2021/05/versionbits_period_start
	9152 sweepprivkeys-29+knots					f3408c3b81d
	(CHECK-LAST)	last=641c2231d37 origin-pull-k/296/head
		# + knots#296
		# NOTE: GetVirtualTransactionSize is safe here because we only support standard p2pk[h] anyway (see 21d85b5c0e)
		# NOTE: Now also includes mintxfee in getwalletinfo for testing purposes
	# Needs work / rewrite to sweepprivkeys? g650 -  # qt, refactor: Add Import to Wallet GUI
	9245 ionice-29+knots						d606cfe65fa
		# low prio: p2p requests, loading/verifying blocks on disk
		# normal prio: connecting blocks, indexes, user requests
	-    ionice_win-29+knots					d91add54320
	8501  old_stats_rpc-29						f4682e37bdc	last=7af0ea43b2
		# Many fixes (incl knots#226)
		# Held back on old version due to conflict with GUI updates...
	8550  old_stats_qt-29+knots					6eb771add8e	last=63fb11652f
		# Held back on old version due to conflict with RPC updates...
		# + knots#377
	9504  rpc_dumpmasterprivkey					c74201144fe	last=07fc81109a
	g444  gui_netwatch-29+knots					fc6c22b6bfa	 # Latest code now
	(CHECK-LAST)	last=191d0fdc9e2 origin-pull-k/330/head
		# NOTE: Was #9849
		# NOTE: Includes #25050 & knots#330
	10615 multiwallet_rpc-29+knots				f28b26d13c7  # latest code now
		# CAUTION: Be extra careful rebasing - diff/patch default context might accidentally move code around between different RPC methods!
		# NOTE: 23.x added restorewallet to preexisting commit d927c064439->c706f7173ad
		# NOTE: Denies backupwallet/dumpwallet/importwallet/loadwallet/dumptxoutset/migratewallet/etc to wallet-restricted users for now
		# TODO: Allow absolutely-denied RPC calls if a RPC whitelist is being used
		# NOTE: Temporarily(?) squashed to obfuscate security fixes (2023-07-28)
	10554 zmq_wtx-29+knots						9a400641041	last=ed4fd266f7  # ZMQ: add publishers for wallet transactions.
		# Extended doc/zmq a bit to match additions from #14060 and #23471
		#30.xTODO# Stop using boost signals!
	20551 rpc_onetry_conntype					eced1e311a1
		# NOTE: Originally based on #12674
		# REBASING NOTE: Ensure any new types get added ? (unless we want to deprecate this...)
	10593 relax_invblk_punishment-29.1+knots	b2170a7ddb0
		# Squash "QA: Use addconnection rather than addnode onetry" ?
		# FIXME: HandleFewUnconnectingHeaders sends getheaders _and_ disconnects??
	10350 filtered_witblock-28				0622d602f10	last=3f388ddcd3 CodeShark/MFWB_no_bump_2
		# NOTE: Don't bump protocol version!
	# script debugger needs major reworking: 10729 scriptex								43b88be136
	# script debugger needs major reworking: 10730 scriptflag_strings-mini-0.17			e54fc122c8	last=e2e183bc1f
	# script debugger needs major reworking: n/a   script_debugger-mini					f6d5379567	last=1d3ed0c48a script_debugger
	11750 coincontrol_multiselect				cc43bf12dfa	last=7cec76f81b # Multiselect in coincontrol treewidget and display selected count
		# NOTE: deviated from PR
	11770 rest_fee								aae647a1719	last=eff1b3e201  # [REST] add a rest endpoint for estimatesmartfee, docs, and test
		# Fixed a minor bug in conf_target range check
		# Added new tests in feature_fee_estimation
		# Updated to match estimatesmartfee RPC changes
	11803 bugfix_dumpwallet_hdkeypath			3fb71a586ad
	12965 scriptthreads-29+knots				245634f180e	last=dfab6c6866 jonasschnelli/2018/04/svt
	13203 dsha256_power8-29						d86c64377f3	last=3b402e0738 TheBlueMatt/2018-05-asm
		# NOTE: Stripped out benchmark change
		#29.xTODO# Watch for Makefile.am or other changes for shared libbitcoinkernel on Windows
	15218 postibd_flush-28						192979c1840	last=8887d28a014  andrewtoth/flush-after-ibd
	15428 tor_gui_pairing-29+knots				1d0040227dc	last=ab9ed21dc98 tor_gui_pairing-0.21+knots
		# Implicitly relies on gui#506 for QR Code without text being centred (dropped buggy 4a881554991)
	15421 tor_subprocess-29+knots				6d51c900303	# Latest code now
		# + knots#352
		# FIXME: fix automatic tor outbound using subprocess
		# FIXME: -netinfo doesn't show tor if inbound-only?
	# TODO: tor guix bundle!
	#30.xTODO# 16490 maflcko/1907-rpcMempoolWhyReplacable
	#	TODO: Diff-minimise
	#	TODO: Support TRUC & Knots policies
	17795 gui_console_ctrl_d-26+knots			35617aeea43
		# NOTE: Completely rewrote to work on all platforms, in addition to Ctrl-W
	15861 restore_vbits_warning					67bc541219b
	n/a   rpc_compat_error_index-25+knots		8db48fd76f7
		# Compatibility with 0.19.0-0.21.0 bech32_error_detection
	g537  gui_bech32_errpos						54e50a9b45f
	17636 guisettings-0.21						e04e292b839	last=187f9684e03 emilengler/2019-11-guisettings
		# Held back 5266efa964b..187f9684e03 (too strict error checking?)
		# (and removed release notes)
	17958 rpc_getgeneralinfo					e38cdb91045	last=cdbd38df131  # getgeneralinfo RPC
	18223 blockfilter_v0						8809410b43e	last=5561e7a0c79
		# NOTE: Don't enable with -blockfilterindex=1
		# NOTE: Diff-minimised
	19089 cli_getinfo_mwbalances-29				8b1a4ab4d0b	last=865d2c32d5a jonatack/cli-getinfo-multiwallet-follow-ups
	19092 cli_getinfo_mw_total_balance-29+knots	7e9b3f5b08d	last=08ac1abc583 jonatack/cli-getinfo-multiwallet-total-balance
	(CHECK-LAST)	last=71bfa1fb715 cli_getinfo_mw_total_balance-26
	19117 rpc_getrpcwhitelist					9efbf736e05
		# NOTE: Was #18827 before any Knots merge
	-     getrpcwhitelist_wallets-29+knots		57caa6a62d1
		# NOTE: when #19118..#19120 get merged, add 71294ee9799
	# Needs purpose: 21815 prayank23:max-out-full-relay
	-     wallettool_dump_warning-29+knots		64c9789ba61
	# Needs work: 22708 hebasto:210815-wayland
	# Needs concept review: 24121 -  # wallet: treat P2TR address with invalid x-only pubkey as invalid
	# Needs work/review: g539  RandyMcMillan-g/1643263956-network-graph-issue-532
	# Needs concept review: 26365 -  # wallet: GetEffectiveBalance
	# Needs concept & review: Only when sending GETBLOCKTXN anyway? (more likely with Knots) 27086 -  # [WIP] p2p: Add random txn's from mempool to GETBLOCKTXN
	30951 v2onlyclearnet-29+knots				970ff980fc3	last=7c6b70d7286
		# Made a hidden option
		# NOTE: -listen=0 required because it doesn't enforce v2 on incoming connections
	# Needs review: 32065 vasild/i2p_early_create_session
	# Needs review & concept: 32726,32728 -  # Add initial OpenAPI/Swagger specification for Bitcoin Core RPC and REST interfaces
	# Needs review: 33044 fanquake/19513_rebased
	# Needs concept & review: 35027 8144225309/net-bind-outgoing
	# Needs concept & review: 35054 fjahr/2026-02-utxo-set-share-safe-take-2
	-     font_for_money_global					b1c8fad52db
	k157  qt_darkmode-29+knots					2906e242972	last=2c15a2071f6 bigshiny90/v29.1-knots-rc1-guifixes
	(CHECK-LAST)	last=aa6b9665628 bigshiny90/gui-darkmode-updates  # knots#160
	# TODO: validaterawtransaction with UTXO lookup (and fee calc) ?
	# TODO: Guix: When glibc 2.36+ is required, use -Wl,-z,pack-relative-relocs
# Non-upstreamed functionality:
	-     rm_tarball_ci-29+knots				2068f85bddf
	# TODO: Revert #25898 ? (Dropped WSL1 compatibility)
	-     restore_upnp-29.3+knots				2745c44169a
	(CHECK-LAST)	last=07f0df46fba origin-pull-k/196/head
		# NOTE: Includes knots#196
		# NOTE: Includes #30301 theuni/miniupnp-228-bump
		# CAUTION: Complex merge with pcp_dont_spam_unauth-29 to avoid enabling full PCP warnings when only UPnP is toggled
		#30.xTODO# Revert #32500
	n/a   restore_feefilter_opt					0562fef9a34
	-     gui_payreq_textedit					a3cfe4a8dd2
	(CHECK-LAST)	last=cad6d027fd7 origin-pull-k/332/head
		# Includes knots#332
	# NOTE: Restoring BIP70 would require restoring OpenSSL, protobuf, and Qt's OpenSSL support :(
	-     rpc_mempoolentry_txhash				0902751ac48
	# FIXME: -     walletnotify_w_win-27+knots			c892f8b6dbf	# Latest code now
		# FIXME: this is broken :(
NM	14137 win_taskbar_progress					fad587754f7	last=18eb4dbb8a
		# Replaced with:
	k215  win_taskbar_progress_com-29			82d94084f6d	last=5f4e34a556d kwsantiago/kwsantiago/191-win-taskbar-progress-qt6
	-     restore_blockmaxsize					cdef21b8014
		# TODO?? blockreservedsize option
	#30.xTODO# Revert #32654 (deprecate blockmaxweight)
	7107  qtnetworkport-29.1+knots				db7ed37417a	last=1f37c87d8f2 origin-pull/7107/head
		# FIXME: Unbind IPv6 on the other port, if its IPv4 bind failed
	7533  sendraw_force-29.2+knots				77ce3499dad last=2627c0937f8 sendraw_force
		# NOTE: overriding anchor-not-empty does not require also overriding non-mandatory-script-verify-flag-upgradable-witness_program UNLESS RDTS is also merged
		# NOTE: partial re-PR in #20753 by Marco
		# TODO: Compatibility with #25532,#29060 if merged
		# TODO: 1d3fdc1adde Support ignoring various rejection reasons in PackageMempoolChecks
			# error message change impacts a bunch of functional tests; and submitpackage currently lacks support for ignore_rejects anyway
	11082 rwconf-29+knots						640a565ed84 # Latest code now
		#30.xTODO# Squash fixes
		#30.xTODO# Deprecate with settings.json better?
	7510  rwconf_gui-29.1+knots					d23c3fe957d
		#30.xTODO# Squash fixes
		#30.xTODO# Move blockreconstructionextratxn (and others?) from rwconf_policy?
		# TODO: when we can enable block filters post-pruning, revert 81d696e132c
	559   accept_nonstdtxn						e6f77cd55c6
		#30.xTODO# Revert or redefine #29843 if it got merged
	929   tbc									147cbbf9ede
	n/a   tbc_font								b4097c6014a
		# Includes ff7b90dc729 Embedded font: Rename to avoid confusion in font selector  (fix_qt_fontsel_confusion)
	 553 bugfix_qt_uri_amount_parser			8efda515c8c
	5861 gui_restore_addresses					aae821323ed
	5891  qt_console_history_persist			bf88af8cd3c	last=2e1d9cb3466 qt_console_history_persist
	(CHECK-LAST)	last=6a5537ab675 origin-pull-k/203/head
		# Includes knots#203 (Add migratewallet RPC in historyFilter)
	k214 qt_console_clearhistory-29+knots		676ef5cfc38	last=d6ded3f4441 kwsantiago/kwsantiago/204-clearhistory
	-     net_identify_librerelay				646572e784b
	-     net_identify_utreexo					2a4f8dd0e86
	-     net_identify_rdts						2c5ac706ec2
	# TODO? petertodd has a branch with 4 extra outgoing peers requiring RBF service flag
	# TODO: some way to add UA comments via rwconf
	12146 opt_wallet_segwit2					0e4f9128875
		# TODO: Split out legacy address preference to be more explicit
		# FIXME? descriptor wallet migration doesn't take this into account?
	# TODO: Rework 17132 (update notification) over Tor for Knots only (and maybe generic alert instead of update-specific)
	# TODO: Consider KUserFeedback telemetry?
	-     gui_wallet_displayname_wo_dat			2c24eaf1c03	# Latest code now
	-     gui_request_payment_label-0.19		c5ba3369fa6
	-     gui_peers_sort_network-23				4eb9223b3ad
	-     gui_peers_no_net_column				bfa129dae82
	# 22439 guix_in_gitian-23+knots				2014b1271e3	last=ebda0463748 achow101/guix-in-gitian
		# FIXME: If restoring, test that this still works (WIP fixes in stash fa8517a9112 but need rebase too)
	-     rpc_getblockfrompeer_future			fac8da1e97a
		# Revert of #23927
	-     rpc_getblockfrompeer_wo_header		d0673ac45ea
		# Prior Knots bundled this in with #20295
	# TODO? * 4b6813a95bd wallet: trigger MaybeResendWalletTxs() at startup (+ 1 second)
		# See #25922, backported with this in 21.x
	# Needs concept acceptance: 26469 -  # rpc: getblock: implement with block height as input parameter.
	32547 mining_avoid_block_copy-29+knots		4367ab06fde	last=7d05ec01d4e mining_avoid_block_copy
	-     gbt_rpc_options-29+knots				ac1ce93090e
	# TODO: pre-cache GBT call after new block?
	#30.xTODO# RPC to get/set policy configs
		# https://github.com/bitcoinknots/bitcoin/issues/115
	#30.xTODO# -     miningcbtag-27+knots
		# TODO: add to rwconf_policy: 4b38a3031ab GUI/Options: Add miningcbtag via settings
	-     blockview-29+knots					a76e0914ec3
	# Needs work: k225  1440000bytes/blockview-txid
	#-     mapport_default_on-27+knots			a32f282230d
		# Re-disabled in light of continued security issues
	#30.xTODO# Look into making the patches tarball in guix
	-     restore_libconsensus					a7b1dc9f4bf
		# +Needs review: 24994 hebasto/220426-consensus
	# TODO: bump dbcache to 1 TB on systems we can detect memory pressure! - after testing
		# https://github.com/bitcoinknots/bitcoin/issues/70
	# TODO: GUI & first run dbcache setup?
	-     rpccookieperms_log_improvements-29+k	78cdc0c6606
	# Needs work: n/a   macos_dmg-27							d26ae740b99
		# Reverts #28432, #28932, and #28973, and includes fix_dmg_openfinder
		# 30.xTODO: revert macos ZIP only: #29733
		# TODO: Investigate if we can compress again by reverting #24031 using patches in https://bugzilla.mozilla.org/show_bug.cgi?id=935237
		# FIXME: Probably incompatible with MERGED #31407 macos_notarization ?
		# TODO? 17311 RandyMcMillan:fix-background-svg
	# Needs review: 31065 danielabrozzoni/20241008_rest_broadcast
	33023 qa_cb_extratxs-25						3be5e3c5bc9	last=841b3c2e966 bigshiny90/compactblocks-extratxs-tests-core
		# Held back f9c6331cb26...841b3c2e966 for now
	#30.xTODO# Revert #32450 ?
	#30.xTODO# Revert #32510 or replace extratxn pool
	k171  Raimo33/add-dockerfile				f151270ccf2	last=4b778a21835
	k187  Retropex/dnsseed-leo					914a920ac1e	last=68abc8a3262
	# Needs work: k194 -  # gui: Implement two-row status bar with centered progress display
	# Needs review? k197 qt_portmap_ux_underlisten
	# Needs work: k208 1440000bytes/sendtx-ui
	k262  index_prune_error_suggestion-29		d75d1f0fa39	last=08574e0aa23 privkeyio/fix/87-blockfilterindex-pruning-startup
	# Needs concept: k270 privkeyio/compile-tr-native
	# Needs work: k274  umop/toggle-banned-peers-visibility
		# NOTE: 7c1a63c0b22 rebased/cleaned up in 31a011d9252, just has extra padding when no bans
	# Needs concept & review: k283 cal-gooo/qt-theme-toggle-fusion
	# Needs concept & review: k286 Bortlesboat/gui-warn-missing-config
	k288  qt_syncprogressbar_fullwidth-0.7		dc44700a648	last=45e89eed5b9 SpectrGen1/issue-177-better-progress-bar
	k297  qt_sweepprivkeys-29					1ca2e769dd5	last=2e165cdffc5 privkeyio/gui-sweep-privkey
# Non-upstreamed policy options (default off):
	30232 refactor_isstandardtx_mpopts-29+knots	d93023c807c
	-     pol_acceptunknownwitness				e7a617a1146
	-     mining_priority						2e4d71bc2bb	# Latest code now
		#30.xTODO# FIXME: Should blockmintxfee apply to blockprioritysize??
		# If mempool-knots.dat is ever extended to store easily manipulatable data, port Xor stuff over
		# Reverts (needed and better performance & memusage): d0cd2e804ec [refactor] rewrite BlockAssembler inBlock and failedTx as sets of txids
		# Reverts (needed for lock logic): 192dac1d337 [refactor] Cleanup BlockAssembler mempool usage
	7219  rbf_opts-29+knots						21872352ab1	# Latest code now
	-     truc_opts-29.2+knots					0db5fb68738
	#TODO/Needs work: 10823 greenaddress/replace-by-fee-old-transactions
	29309 permitbarepubkey-29+knots				fc017ba645d	last=1dfe27e49ab
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     bytespersigopstrict-29+knots			e9cec28d253
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	9749  unique_spk_mempool-29.2+knots			9accdcb973d
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
	-     dustdynamic-29.1+knots				7c35ab55b63
	# ---- BEGIN DATACARRIER ---- (OLGA not backported)
	28408 match_more_datacarrier-29+knots		a40cd352e5b	last=4d2ec0671a3 match_more_datacarrier
		#30.xTODO# TODO: Delete TBD "maxdatacarriersize" from #29954 (see b02aab950af) (or at least fix the description)
		# Adds sendraw_force compat & config option to restore old behaviour (for -corepolicy later)
		# TODO? Revise byte counting to consider input/output waste
	-     datacarriercost-29+knots				c7f2ccced12
		# + knots#268 (partial; remaining in rwconf_policy)
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		#30.xTODO# Add tests and make sure boundaries are correct
	-     acceptnonstddatacarrier-29+knots		686db258c77
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# FIXME: Data before OP_RETURN (and non-push opcodes??) should count the data as non-standard (but can't predict everything, so wait until there's a need? 75f1652b447)
	# ---- END DATACARRIER ----
	k136  pol_permitephemeral					ef266950b82
		# Also includes permitbare{anchor,datacarrier} options
		# FIXME: prioritisetransaction shouldn't block dust txs (but also shouldn't blindly bypass policy by promoting ephemeral to non-ephemeral!)
	# TODO: Filter for output value < tx fee * N - https://twitter.com/DoctorBuzz1/status/1741622696327205176
	# TODO: Impose accurately-calculated (not just guessing witness size) dust limit on Taproot _spends_ (only Taproot because there should be a more sensible spend path available in theory)
		# https://github.com/bitcoinknots/bitcoin/issues/113
	# TODO: #28400-based match_more_datacarrier? Needs work, but ee8e79a7455 limits to policy
	-     rejecttokens-29.1+knots				374c6f4b520
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
		# Currently filters just Runes
	k349  privkeyio/policy-reject-counterparty	3b81083acf2	last=7b1d8136181
		# TODO: Needs review
	k78   rejectparasites-29.1+knots			09a886f82c4	last=d978324923a
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
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
		# Classifier scripts; could be set for valid (dangerous), track for fee estimation, relay, mine [decided at mine-time so multiple policies possible?; at a lower priority?], etc
	# Needs concept ACK and review: k107 Retropex/maxfee
	# Needs concept ACK: 29843 ajtowns/202303-acceptnonstdscript  # allow using upgradable nops
	# Leaving out #27261 (Ignore datacarrier limits for dataless OP_RETURN outputs) because same behaviour already exists for -datacarriersize=1 and this adds corepoicy complexity - REVISIT IF PR is changed to allow only necessary outputs (value burnt or lone output)
	-     maxscriptsize-29+knots				3ce9138865d
		#30.xTODO# TODO: Add to getmempoolinfo like #29954 (see b02aab950af)
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
	# TODO? k146 Option to reduce effective fee by dust for each anchor/op_ret
	k148  minrelaymaturity-29.1+knots			572713a5702
	# TODO? k147 Option to factor coin-age priority into vsize
	#30.xTODO# Revert or make optional changes to OP_RETURN policies like #32359,#32381,#32406
		#30.xTODO# Ensure #32790 doesn't break
	# Needs review? 32453 JeremyRubin/unsigned_annex
	# Needs review: 33682 -  # More comprehensive datacarrier configuration
		# See also #33690
	# Needs review: 33759 roconnor-blockstream/bip143-standardness-2025-10
	# Needs review & optionality: 35225 pinheadmz/p2ms-nonstandard-nonminimal
	-     pol_maxtxlegacysigops-29.1+knots		5233d2ee298
		# Made user-configurable and overridable
	-     blockreconstructionextratxnsize		47ec402c51b
		# TODO: Consider knots#218
	# Needs review? k221 1440000bytes/getextrapoolinfo-rpc
	# Needs work: k227 1440000bytes/remove-minedtxs-extrapool
	k162  qt_bad_external_signer_msg-22			22c27c35066	last=111c401fc5a bigshiny90/fix-invalid-scriptsigner-errordialog
	# Needs work: k271  privkeyio/policy-tapscript-dust-limit
	k272  subdustfeepenalty-29.3+knots			e5991550fa8	last=af7d6f6adba privkeyio/policy-subdust-fee-penalty
		# Partial: remaining in rwconf_policy
	# Needs review: k275  privkeyio/feature-rbf-feerate-mode
	# Needs review: k280  privkeyio/feature-priority-vsize-discount
	k292  datacarrier_opnet-29+knots			660d20024af	last=6938c68fe68 Retropex/rework-opnet
	# TODO? Dust multiplier by # of outputs: https://x.com/snapolino/status/1976708308603224518
# Non-upstreamed Knots compatibility:
	#30.xTODO# maybe revert #33214 rpc: require integer verbosity; remove boolean 'verbose'
	#30.xTODO# maybe revert #32721 achow101:remove-deprecated-balances
	#30.xTODO# -     compat_bumpfee_require_replacable
		# 5777b0d6319 RPC/Wallet: bumpfee: Default require_replacable=true if local mempool policy is not full RBF
		# e32b75202da RPC/Wallet: Check deprecatedrpc=require_replacable in bumpfee method, to match previous behaviour
		# 386e285943d (rebase on c79ee09a786 needed)
		# c79ee09a786 RPC/Wallet: Add "require_replacable" option to bumpfee method, to match previous behaviour
		# 1f1259d318d GUI/Wallet: Warn if bumping the fee on a non-BIP125 transaction
	-     compat_rpc_dumptxoutset_hr			3aa3d1d84d9
		# FIXME: 'type' param attempts to parse as JSON ? (with 28.x bitcoin-cli tho)
		# FIXME: 'rollback' param rejects height ?
	-     compat_jsonrpc_weirdversions			2411d7211d5
	29530 rpc_getpeerinfo_misbehaving_score-29+k	3defda8ad24	last=87efb6f0cfd
		# NOTE: Held back 976d61c974e...87efb6f0cfd which degrades docs and adds a test incompatible with Knots
		# Deprecated in Knots 28.1
	-     rpccookieperms_octal_compat-29+knots	60c871e8203
	-     zmq_ipc_uri_compat					4f98b2f2447	last=0b1762c90d1 origin-pull/28020/head
		# Backward compatibility with #28020 URI format supported by Knots 25.1+
	#30.xTODO# Check on #29942 removal of -datacarrier, possibly revert?
	# TODO: -netinfo and other version checks might need to be more flexible?
	-     wallet_undeprecate_legacy-29			ee810a31b06
		#30.xTODO# consider deprecating it
		# Effectively reverts #24505, #27869, #28597, and gui#764
		#30.xTODO# revert? #32438 refactor: Removals after bdb removal ... #32440 #32448 #32449 #32452 #32459 #32476 #32481 #32511 #32459 #32523 #32569 #32596 #32618 #32619? #32620? #32758 #32768? #32944? #32977?(might need #33041 to replace it?) #32990? #33032? (replace #33064->#27593??) #33075 #33082? #33161 #33179
		#30.xTODO# revert #28710  Remove the legacy wallet and BDB dependency
		#30.xTODO# revert #31250  wallet: Disable creating and loading legacy wallets
	14641 fundraw_min_conf_deprecated-25+knots	939e1b00067	last=55a0b4c0f90 promag/2018-11-fundrawtransaction
	-    preserve_unsupported_keyflags			a7bc568a076
	-     netperms_implicit_addr				03db9275bf3
	-     rpc_getblockfrompeer_nodeid_compat	98d8860d00d
	# TODO: add a bitcoinknots.conf ?
	n/a   gui_peers_bump_setting_keys-29+k		f708a222a6f
		#30.xTODO# Each release, see if we need to bump setting names for GUI states
		# git grep 'alue(.*State\|toByteArray\|saveState'
		# Window position/size: leave alone
		# Splitter position: leave alone? but syncronise with header columns appropriately
		# Header columns: need a rename
# POLICY:
	-    1day_default_conftarget				4bc27937225
	# Needs work/option: 24106 -  # policy: treat P2TR outputs with invalid x-only pubkey as non-standard
	# Disabled just to be safe: -     bloom_default-29+knots				401f2f03e86
		# Take typo fix from def_bloom_local_only
	-     def_bloom_local_only					b45011c5881
		# NOTE: Includes typo fix
	-     wallet_avoid_newerchange				a4d73445e59
	-     enforce_checkpoints					2ad447bd38b
		#30.xTODO# Revert #31649
	n/a   checkpoint_update-29					7306557b8b0
		# TODO: update (see #34677 -> knots#291)
		# TODO: Do https://github.com/bitcoin/bitcoin/pull/31940/files ?
		#30.xTODO# Revert #25725 (Remove mainnet checkpoints)
	# TODO: revert #28354 ?
	10282 softwareexpiry						d6327766d43
	(CHECK-LAST)	last=2f53648f1a2 privkeyio/fix-gui-datetime-locale
		# + part of knots#336
		# Needs work: + knots#247
		# TODO: "OK" is probably the wrong button to use for this
		# TODO? "Upgrade" button to open website - or even download+verify??
			# -DUPGRADE_COMMAND='...' for PPA/etc?
	-     rwconf_policy-29.3+knots				ad5dce8016a
		# + knots#245
		# + knots#197 qt_portmap_ux_underlisten (ideally, move this to its own merge, but that requires CreateOptionUI etc split out of rwconf_policy)
		# + knots#268 (partial; remaining in datacarriercost)
		# + knots#272
		# TODO: + knots#281
		# Includes Knots policy changes for simplification of final rebase process
		#30.xTODO# Ensure LimitOrphanTxSize sets everything needed still
		#30.xTODO# Check on block assembly GetArgs like blockmintxfee/etc
		#TODO: Add segwit wallet stuff?
		#TODO: Get GUI settings for dustdynamic to select ratio box & focus text area when you click their labels
		#30.xTODO# QTreeWidget or similar for GUI Options dialog?
	# Needs review: 22698 mjdietzx:fix_bip125_inherited_signaling
	#30.xTODO# Needs review/argument/optional? 22779 darosior:taproot_dust_limit
	# Needs review: 22871 JeremyRubin:discourage-csv
	# Needs review/options: 23121 glozow:ancestorscore-remove-bip1252
	# Needs review/options: 26348 -  # Make P2SH redeem script "IF .. PUSH <x> ELSE ... PUSH <y> ENDIF CHECKMULTISIG .. " standard
	# Needs refactoring to only happen for -acceptnonstdtxn(?): 26398 instagibbs/relax_too_small_tx_equality
	# Needs review & optionality: 26451 sdaftuar/2022-11-fixrbf
	# Needs concept & review: k217 1440000bytes/feefilter-extrapool
	k354  rejecttokens_def-29+knots				7554e8e9794	last=792dae6539a pdath/rejecttokens
		# Added corepolicy
# HARDFORK:
	# Disabled: k289  rdts_not_enforced_prompt
	k238 rdts_combined-29+knots					0f345619b10	last=f62f5fda667
	(CHECK-LAST)	last=28187c41c8e rdts_consent_prompt
	(CHECK-LAST)	last=d58e6f82909 origin-pull-k/323/head
	(CHECK-LAST)	last=522df02219f privkeyio/rm-rdts-consent
		# + knots#256 + maxstaleoutbound + maxstaleoutbound=8 + knots#323 + fixes + knots#362
		# TODO: + updated fixed seeds ?
		# NOTE: Core PR in #24930
	k320  miniscript_guard_tapscript_opif-29	4bf46ec4dcc	last=74a8dd54ae8 privkeyio/rdts-guard-opif-tapscript
	k348  Retropex/seeds-knots					106ccd5f5c3	last=3ca6d37783e
	k350  privkeyio/correct-rdts-invalid-blocks	ab0eef9f5fd	last=e8a82740997
	k359  pow_hf_blake2b						6889244bdac
	k357  sighash_unified-29.3+knots			9f4e0454e94	last=54d757f269d privkeyio/hf-sighash-opt-in
		# TODO: Needs review?
	k358  rdts-flagday-29+knots					796600fc2bd	last=ce671c29ff5 chrisguida/rdts-flagday-29+knots
		# TODO: Needs review?
	k363  rpc_blockheaderv2-29+knots			eef1c1181d2	last=2736df8e879 AcesHigh70/rpc_v2_header_fields
		# TODO: Needs review?
	k368  blake2b_servicebit-29+knots			49499d010f2	last=e9f3af467e2 chrisguida/blake2b-servicebit-29+knots
		# TODO: Needs review?
	k386  blake2b_rapid_dns-29+knots			000dd869300	last=f4004d5fcf9 privkeyio/blake2b-dns-immediate-when-no-hf
		# + tidy fix
	k385  pow_hf_blake2b_params					6074239ef0f
# Pre-BRANDING: (might need to be part of F patch to eliminate binary files)
	n/a   (delete_release_notes_fragments)		6c403f501a7
	# Triage: 34808 hebasto/260311-qt-ts-source
	7483  svg_icon-29.3+knots					4a8e99cd037
	(CHECK-LAST)	last=c198e9b3586 origin-pull-k/328/head
		# Consider: https://github.com/bitcoinknots/bitcoin/pull/54
		# Includes knots#328
# BRANDING:
	n/a   upd_copyrightyear-29					4439e39c9ae
	n/a   font_ocrbitcoin						2f826b891fc
	n/a   knots_branding-29						4923d3a6b19
		# NOTE: Includes #33422 to clean up "(64-bit)" leftovers
		#30.xTODO# Review security policy
		# FIXME: Get NSIS using OCR-Bitcoin
		# NOTE: Includes knots#211
# FIXME: Avoid dupes of | * fee3f9ba248 (rpcarg_type_per_name) RPC: Support specifying different types for param aliases
# FIXME: Check hidden_args has anything removed (possibly conditional)
#30.xTODO# FIXME: Make sure there's no duplicate commits (eg, due to a +knots with stale merges): git log --pretty='%s' v0.19.0.1..|sort|uniq -c |sort -n|tail
#30.xTODO# Ensure #32514 is applied to Knots changes
# TODO: Ensure no #include <config/bitcoin-config.h>
# TODO: Check that we aren't deprecating anything in Core
# TODO: Check net_permissions.h for overlapping NetPermissionFlags
# TODO: Ensure 83aa95039d0 doesn't expose any new bugs
# TODO: Check that no git Author lines are a mix due to GIT_AUTHOR_NAME no longer allowing emails: git log v27.1.. | grep '^Author.*luke-jr' | grep -v Dashjr
# TODO: test build with Boost 1.73
# TODO: test fuzzer with everything enabled
	n/a   (cherrypick=488640fe20b)				08ef756ea4b	# doc/{bips,files}
		# TODO: Update with bump_version below !!!!
	n/a  (bump_version=knots20260508)			bd2bfed0acc
	n/a  (cherrypick=12816ba10df)				3acee1b5069	# bump to 29.4.1
#	n/a  knots_historical_relnotes				61100a2
	n/a   rm_historical_relnotes_from_dist		8309251af1d
	n/a   (cherrypick=b9682b0a548)				b9682b0a548  # release notes: write/update, including change log and credits
		# WHEN UPDATING: Remember to check for new authors/co-authors for credits
		# git log --pretty=%s v0.20.0..v0.20.1.knots20200815 >lol && perl -nle 'm[^- #(\d+) (.*) \(.*?\)$] && print "$1 $2"' doc/release-notes.md | while read prnum subj; do grep "\\b$prnum\\b\|\\Q$prbody\\E" lol; done
		# git log --pretty=%s v0.18.0..v0.17.1.knots20181229 >lol && lol v0.18.0..|while IFS= read -r g; do s=$(perl -nle 'm/^.*\*[ \\|]* ([\da-f]{10,})( \(.*?\))? (.*)$/ or exit; $_=$3;s/^(Merge [gk]?\d+ ).*/$1/;print' <<<"$g"); if [ "$s" = "" ]; then echo "$g"; elif fgrep -q "$s" lol; then echo "$g"; else echo $'\033'"[0;31m$g"$'\033'"[0m"; fi; done|less -R
		# git log --pretty=oneline --abbrev-commit > lol && grep '^-.*`.*` \*' doc/release-notes.md|while IFS='`' read a b c; do grep -q $b lol && continue; grep "$(echo ${c:2} | sed 's/ *(.*$//')" lol || echo "$a\`\`$c"; done
		# Make sure no binary files added!
		# remove changelog entries that were in Knots already
		# remove asterisk in changelog for what's been merged last-minute, update doc/files etc
		# git diff|grep '^+.*`'|cut -d'`' -f2|while read c; do grep -q $c lol || echo $c; done
		# When re-added, #28824 notes in 9db5d23d559
		# When re-added, #33259 notes in 32695dff9e6
	n/a  (cherrypick=8c85b1585da)				8c85b1585da  # update manpages (build first)
		# WARNING: Don't forget to add zsh completion!
		# WARNING: Need to build as CMAKE_BUILD_TYPE=Release to avoid 'lock' log level being in manpages/config
		#30.xTODO# check all applicable build options are enabled (see also #33085 and #33828, plus miniupnpc)
		# also example bitcoin.conf and bitcoin-cli bash-completion
	#29.xTODO# n/a  (cherrypick=9b1226db50e)				a5eb5c7e301  # translation update
		# TODO: Upload to Transifex with * d9411324066 (ts_20220515, origin-pull-g/599/head) GUI: Support translating Bitcoin units
		# TODO: git grep --perl-regexp '＆|％|&amp;amp;|&lt;(?:numerusform|source|translation)|&(?!(?:amp|lt|gt|quot|apos);)' src/qt/locale/*.ts
# NOTE: use git diff --minimal for patches!

# TODO: @29.x-knots-android
	# 32262 hebasto/250413-android
	# 34211 build: Alt restore cross-compilation for Android

# TODO: @29.x-knots-extratests
	# TODO: 31367 dergoegge/2024-11-ci-ulimit-s
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
